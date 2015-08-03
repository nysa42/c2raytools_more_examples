# PURPOSE: Program to calculate the ionized fraction (by volume and mass) and store into a file
# INPUT: The density and xfrac files from C2Ray and a redshift file (currently, CubeP3M)
# OUTPUT: A txt file with z, iof_vol, iof_mass and a basic plot
# USAGE: Be sure to set the paths, names, and mesh appropriately
# AUTHOR: Keri L. Dixon 27.09.2013

import c2raytools as c2t
import numpy as np
import glob
import os.path

#Filenames and path
#density_path = '/research/prace/sph_smooth_cubepm_130627_12_6912_500Mpc_ext2/global/so/nc300/'
density_path = '/research/prace/sph_smooth_cubepm_130329_10_4000_244Mpc_ext2_test/global/so/nc250/'
#density_path = '/research/prace/sph_smooth_cubepm_130315_6_1728_47Mpc_ext2/nc306/'
xfrac_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2S_250/results/'
output_filename = './results/meanG_244Mpc_f2_8.2S_250.dat'
z_filename = '../reds_full.dat'

# Read in z file to get snap and redshift and set mesh
z_arr = np.loadtxt(z_filename, unpack=True, skiprows=1)
z_min = 10
thresh = 0.1

out = open(output_filename, 'w') # open output file

#Loop over z
for i in range(z_min,len(z_arr)):
    print 'z = %.3f'% (z_arr[i])
    density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat'%(z_arr[i])))
    if not density_file:
        density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat'%(z_arr[i-1])))
    print 'Desnity file = %s' % density_file
    dfile = c2t.DensityFile(density_file)

    #Delta = dfile.raw_density/np.mean(dfile.raw_density.astype('float64'))

    xfrac_file = ''.join(glob.glob(xfrac_path+'xfrac3d_%.3f.bin' % (z_arr[i])))
    print 'Ionized fraction file = %s' % xfrac_file
    xfile = c2t.XfracFile(xfrac_file)

    irate_file = ''.join(glob.glob(xfrac_path+'IonRates3_%.3f.bin'%(z_arr[i])))
    print 'Ionization rate file = %s' % irate_file
    ifile = c2t.IonRateFile(irate_file)
   
    avg_vG = ifile.irate.mean()
    avg_mG = c2t.mass_weighted_mean_xi(ifile.irate,dfile.raw_density)
    avg_xIIG = c2t.mass_weighted_mean_xi(ifile.irate,xfile.xi)
    median_vG = np.median(ifile.irate)


    ilist = np.reshape(ifile.irate,(ifile.mesh_x*ifile.mesh_y*ifile.mesh_z,1))
    Dlist = np.reshape(dfile.raw_density/np.mean(dfile.raw_density.astype('float64')),(ifile.mesh_x*ifile.mesh_y*ifile.mesh_z,1))
    avg_dG = 0.
    count = 0
    for index,Delta in enumerate(Dlist):
        if (Delta < 1. - thresh): continue
        elif (Delta > 1. + thresh): continue
        else:
            #print 'index = ',index, 'and Delta = ',Delta
            avg_dG += ilist[index]
            count += 1
    avg_dG /= count
    print 'count is ',count,' compared to grid of ',ifile.mesh_x*ifile.mesh_y*ifile.mesh_z

    print 'z, avg_vG, avg_mG, avg_xHII, median = %.3f %.4e %.4e %.4e %.4e %.4e' % (z_arr[i], avg_vG, avg_mG, avg_xIIG, median_vG, avg_dG)
    out.write('%.3f %.4e %.4e %.4e %.4e %.4e\n' % (z_arr[i], avg_vG, avg_mG, avg_xIIG, median_vG, avg_dG))

out.close()
