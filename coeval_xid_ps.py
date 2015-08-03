## PURPOSE: Program to calculate mean, rms, and skewness of dT for coeval cubes with and without                                        
#          redshift space distortions and with and without smoothing.                                                                              
# INPUT:   The dT and dT_pv box files generated from make_dTboxes.py                                                 
# OUTPUT:  Two txt files with z, nu, mean, rms, skewness, smoothed mean, smoothed rms, and                                 
#          smoothed skewness for redshift space distortions and not                                                                                   
# USAGE:   Be sure to set the paths, filenames, max z, and smoothing parameters                                                                    
# AUTHOR:  Keri L. Dixon 17.04.2014                                                                                                             


import c2raytools as c2t
import numpy as np
import glob
import os.path

# Filenames and path                                                                                               
#density_path = '/research/prace/sph_smooth_cubepm_130627_12_6912_500Mpc_ext2/global/so/nc300/'     
density_path = '/research/prace/sph_smooth_cubepm_130329_10_4000_244Mpc_ext2_test/global/so/nc250/'
#density_path = '/research/prace/sph_smooth_cubepm_130315_6_1728_47Mpc_ext2/nc306/'                                                                   
xfrac_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2S_250/results/'
z_filename = 'red_short.dat'
z_full = '../reds_full.dat'
output_path = './results/xid_ps_244Mpc_8.2S_250_'
out1_path = './results/d_ps_244Mpc_8.2S_250_'

z_arr = np.loadtxt(z_filename, unpack=True)
z_f = np.loadtxt(z_full, unpack=True, skiprows=1)

c2t.set_sim_constants(boxsize_cMpc = 244.)

for i in range(len(z_arr)):
    output_filename = output_path+'%.3f.dat'%(z_arr[i])
    print 'z = %.3f'% (z_arr[i])
    
    density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat'%(z_arr[i])))
    if not density_file:
        zi = np.where(z_f==z_arr[i])
        density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat'%(z_f[zi[0]-1])))
    print 'Density file = %s' % density_file
    dfile = c2t.DensityFile(density_file)

    xfrac_file = ''.join(glob.glob(xfrac_path+'xfrac3d_%.3f.bin'%(z_arr[i])))
    print 'Ionized fraction file = %s' % xfrac_file
    xfile = c2t.XfracFile(xfrac_file)

    dT_file = ''.join(glob.glob('./dT_boxes/dT_%.3f.cbin'%(z_arr[i])))
    print 'dT file = %s' % dT_file
    dT_box = c2t.read_cbin(dT_file, bits=64, order='F')

    ps_dT,kT = c2t.power_spectrum_1d(dT_box, kbins=75)
    ps_xi,kxi = c2t.power_spectrum_1d(xfile.xi/xfile.xi.mean()-1, kbins=75)
    ps_x,kx = c2t.power_spectrum_1d((1-xfile.xi)/(1-xfile.xi.mean())-1,kbins=75)
    ps_d,kd = c2t.power_spectrum_1d(dfile.raw_density/dfile.raw_density.mean()-1, kbins=75)
    ps_xid,kxid = c2t.cross_power_spectrum_1d((1-xfile.xi)/(1-xfile.xi.mean())-1,(dfile.raw_density/dfile.raw_density.mean()-1), kbins=75)

    if( kT.all() != kxi.all() ): print 'poop'
    if( kT.all() != kd.all() ): print 'poop2'

    factor = pow(dT_box.mean(),2)
    out = open(output_filename, 'w')
    for j in range(len(kT)):
        out.write('%.3f %.4f %.4f %.4f %.4f %.4f\n' % (kT[j],ps_dT[j],ps_xi[j]*factor,ps_x[j]*factor,ps_d[j]*factor,ps_xid[j]*factor))
    out.close()
