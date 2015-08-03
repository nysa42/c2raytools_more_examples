# PURPOSE: Program to calculate the ionized fraction (by volume and mass) and store into a file
# INPUT:   The density and xfrac files from C2Ray and a redshift file
# OUTPUT:  A txt file with z, iof_vol, and iof_mass
# USAGE:   Be sure to set the paths, names, and mesh appropriately
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
output_filename = './results/xfrac_244Mpc_f2_8.2S_250.dat'
z_filename = '../reds_full.dat'

# Read in z file to get snap and redshift and set mesh
z_arr = np.loadtxt(z_filename)
z_min = 10

out = open(output_filename, 'w')

# Loop over z
for i in range(z_min,len(z_arr)):
    print 'z = %.3f'% (z_arr[i])
    density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat' % (z_arr[i])))
    if not density_file:
        density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat' % (z_arr[i-1])))
    print 'Density file = %s' % density_file
    dfile = c2t.DensityFile(density_file)
    #dens_arr = np.reshape(dfile.raw_density,box_vol)

    xfrac_file = ''.join(glob.glob(xfrac_path+'xfrac3d_%.3f.bin' % (z_arr[i])))
    print 'Ionized fraction file = %s' % xfrac_file
    xfile = c2t.XfracFile(xfrac_file)
    #xfrac_arr = np.reshape(xfile.xi,box_vol)

    avg_nHII = xfile.xi.mean()
    avg_mHII = c2t.mass_weighted_mean_xi(xfile.xi,dfile.raw_density)

    print 'z, avg_nHII, avg_mHII = %.3f %.4e %.4e' % (z_arr[i], avg_nHII, avg_mHII)
    out.write('%.3f %.4e %.4e \n' % (z_arr[i], avg_nHII, avg_mHII))

out.close()
