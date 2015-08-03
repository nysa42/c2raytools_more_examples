# PURPOSE: Program to calculate 3D power spectrum (distorted and not) over an entire box
# INPUT: The dT boxes in cbin format and the interesting redshifts, red_short.dat 
# OUTPUT: A text file with 
# USAGE: Change density_path, xfrac_path, z_filename, and z_min to suit the simulation
# AUTHOR: Keri L. Dixon 17.04.2014

import c2raytools as c2t
import numpy as np
import glob
import os.path

# Set path and file names
#density_path = '/research/prace/sph_smooth_cubepm_130627_12_6912_500Mpc_ext2/global/so/nc300/'
density_path = '/research/prace/sph_smooth_cubepm_130329_10_4000_244Mpc_ext2_test/global/so/nc250/'
#density_path = '/research/prace/sph_smooth_cubepm_130315_6_1728_47Mpc_ext2/nc306/'
xfrac_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2S_250/results/'
z_filename = 'red_short.dat'
output_path = './results/75ps_244Mpc_8.2S_250_'
out1_path = './results/75ps_rsd_244Mpc_8.2S_250_'

z_arr = np.loadtxt(z_filename, unpack=True)

c2t.set_sim_constants(boxsize_cMpc = 244.)

for i in range(1,len(z_arr)):
    output_filename = output_path+'%.3f.dat'%(z_arr[i])
    out1_filename = out1_path+'%.3f.dat'%(z_arr[i])
    print 'z = %.3f'% (z_arr[i])
 
    dT_file = ''.join(glob.glob('./dT_boxes/dT_%.3f.cbin'%(z_arr[i])))
    print 'dT file = %s' % dT_file
    dT_box = c2t.read_cbin(dT_file, bits=64, order='F')
    
    dT_rsd_file = ''.join(glob.glob('./dT_pv_boxes/dT_pv_%.3f.cbin'%(z_arr[i])))
    print 'dT_pv file = %s' % dT_rsd_file
    dT_rsd_box = c2t.read_cbin(dT_rsd_file, bits=64, order='F')
    
    print 'Calculating power spectra...'

    ps_raw,k = c2t.power_spectrum_1d(dT_box, kbins=75)
    ps_rsd,k = c2t.power_spectrum_1d(dT_rsd_box, kbins=75)
   
    out = open(output_filename, 'w')
    out1 = open(out1_filename, 'w')
    for j in range(0,len(k)):
        out.write('%.3f %.4f\n' % (k[j],ps_raw[j]))
        out1.write('%.3f %.4f\n' % (k[j],ps_rsd[j]))
    out.close()
    out1.close()
