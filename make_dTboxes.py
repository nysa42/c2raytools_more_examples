# PURPOSE: Program to calculate dT over entire box and save as a cbin file
# INPUT: The density, velocity, and xfrac files from C2Ray and a redshift file
# OUTPUT: A cbin format file with the mesh and dT_box 
# USAGE: Change density_path, xfrac_path, z_filename, and z_min to suit the simulation
# AUTHOR: Keri L. Dixon 17.04.2014

import c2raytools as c2t
import numpy as np
import glob
import os.path

#Filenames and paths
#density_path = '/research/prace/sph_smooth_cubepm_130627_12_6912_500Mpc_ext2/global/so/nc300/'
density_path = '/research/prace/sph_smooth_cubepm_130329_10_4000_244Mpc_ext2_test/global/so/nc250/'
#density_path = '/research/prace/sph_smooth_cubepm_130315_6_1728_47Mpc_ext2/nc306/'
xfrac_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2S_250/results/'
output_filename = './dT_boxes/mean_dT.dat'
out1_filename = './dT_boxes/mean_dT_pv.dat'
z_filename = '../red5.dat'

c2t.set_verbose(True)
c2t.set_sim_constants(boxsize_cMpc = 244.)

# Read in z file, convert to frequency, and set minimum z slice (dependent on xfrac avail)
z_arr = np.loadtxt(z_filename)
nu = c2t.cosmology.z_to_nu(z_arr)
z_min = 0 #10 or 11? if red1 and 0 otherwise

# Open output files for mean dT and dT rms (mainly for checks)
out = open(output_filename, 'w')
out1 = open(out1_filename, 'w')

# Loop over z, read in density, xfrac, and vel, and calculate dT
for i in range(z_min,1):#len(z_arr)):
    print 'z = %.3f'% (z_arr[i])
    density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat'%(z_arr[i]))) 
    if not density_file:
        density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat'%(z_arr[i-1])))
    print 'Density file = %s' % density_file
    dfile = c2t.DensityFile(density_file)

    xfrac_file = ''.join(glob.glob(xfrac_path+'xfrac3d_%.3f.bin'%(z_arr[i])))
    print 'Ionized fraction file = %s' % xfrac_file
    xfile = c2t.XfracFile(xfrac_file)
    
    vel_file = ''.join(glob.glob(density_path+'%.3fv_all.dat'%(z_arr[i])))
    if not vel_file:
        vel_file = ''.join(glob.glob(density_path+'%.3fv_all.dat'%(z_arr[i-1])))
    print 'Velocity file = %s' % vel_file
    vfile = c2t.VelocityFile(vel_file)
    kms = vfile.get_kms_from_density(dfile)

    mesh = (xfile.mesh_x, xfile.mesh_y, xfile.mesh_z)
    print 'mesh = ', mesh

    dT_box = c2t.calc_dt(xfile, dfile, xfile.z)
    dT_file = './dT_boxes/dT_%.3f.cbin' % (z_arr[i])
    print 'dT_box file = %s' % dT_file
    
    #rho = dfile.cgs_density
    #print 'rho_crit*OmegaB',c2t.const.rho_crit_0*c2t.const.OmegaB#*(1+z_arr[i])**3
    #print 'rho.mean()',rho.mean()
    c2t.save_cbin(dT_file, dT_box, bits=64, order='F')

    dT_pv_box = c2t.get_distorted_dt(dT_box, kms, xfile.z, num_particles=40)
    dT_pv_file = './dT_pv_boxes/dT_pv_%.3f.cbin' % (z_arr[i])
    print 'dT_pv_box file = %s' % dT_pv_file
    c2t.save_cbin(dT_pv_file, dT_pv_box, bits=64, order='F')

    dT_mean = dT_box.mean()
    dT_rms_box = np.sqrt((dT_box - dT_mean)**2)
    dT_rms = dT_rms_box.mean()
    dT_rms_other = c2t.rootmeansquare(dT_box)
    dT_pv_mean = dT_pv_box.mean()
    dT_pv_rms_box = np.sqrt((dT_pv_box - dT_pv_mean)**2)
    dT_pv_rms = dT_pv_rms_box.mean()

    print 'z, nu, dT_mean, dT_rms %.3f %.3f %.4f %.4f %.4f' % (z_arr[i], nu[i], dT_mean, dT_rms, dT_rms_other)
    out.write('%.3f %.3f %.4f %.4f\n' % (z_arr[i], nu[i], dT_mean, dT_rms))
    out1.write('%.3f %.3f %.4f %.4f\n' % (z_arr[i], nu[i], dT_pv_mean, dT_pv_rms))

out.close()
out1.close()
