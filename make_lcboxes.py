# PURPOSE: Program to calculate the dT lightcone along three lines of sight with bandwidth and beam convolution
# INPUT: The dT boxes from make_dTboxes.py and a redshift file
# OUTPUT: Two txt files with z, nu, mean, rms for smoothing and not
# USAGE: Be sure to set the paths, names, smoothing, and mesh appropriately
# AUTHOR: Keri L. Dixon 21.04.2014


import c2raytools as c2t
import numpy as np
import glob
import os.path

#Filenames and path
#density_path = '/research/prace/sph_smooth_cubepm_130627_12_6912_500Mpc_ext2/global/so/nc300/'
density_path = '/research/prace/sph_smooth_cubepm_130329_10_4000_244Mpc_ext2_test/global/so/nc250/'
#density_path = '/research/prace/sph_smooth_cubepm_130315_6_1728_47Mpc_ext2/nc306/'
xfrac_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2S_250/results/'
dT_path = 'dT_boxes/'
out_box = './lc_boxes/dT_lc0_244Mpc_8.2S_250.cbin'
out1_box = './lc_boxes/dT_lc1_244Mpc_8.2S_250.cbin'
out2_box = './lc_boxes/dT_lc2_244Mpc_8.2S_250.cbin'
out_pv_box = './lc_boxes/dT_pv_lc0_244Mpc_8.2S_250.cbin'
out1_pv_box = './lc_boxes/dT_pv_lc1_244Mpc_8.2S_250.cbin'
out2_pv_box = './lc_boxes/dT_pv_lc2_244Mpc_8.2S_250.cbin'
file_z = './lc_boxes/out0_z.dat'
file1_z = './lc_boxes/out1_z.dat'
file2_z = './lc_boxes/out2_z.dat'

c2t.set_verbose(True)
c2t.set_sim_constants(boxsize_cMpc = 244.)
z_low = 6.0
z_high = 22.

# Read in dT boxes, get filenames, and make lightcones
dT_files = glob.glob(dT_path+'dT_*.cbin')
dens_files = glob.glob(density_path+'*n_all.dat')
vel_files = glob.glob(density_path+'*v_all.dat')

vel_lightcone, z = c2t.make_velocity_lightcone(vel_files, dens_files, z_low, z_high, los_axis=0)
dT_lightcone,out_z = c2t.make_lightcone(dT_files, z_low , z_high, cbin_bits=64, cbin_order='F', los_axis=0)
rsd_dT = c2t.get_distorted_dt(dT_lightcone, vel_lightcone, z, num_particles=40, los_axis=2, velocity_axis=0, periodic=False)

c2t.save_cbin(out_box, dT_lightcone)
c2t.save_cbin(out_pv_box, rsd_dT)
np.savetxt(file_z,out_z,fmt="%f")

vel_lightcone, z = c2t.make_velocity_lightcone(vel_files, dens_files, z_low, z_high, los_axis=1)
dT_lightcone,out_z = c2t.make_lightcone(dT_files, z_low , z_high, cbin_bits=64, cbin_order='F', los_axis=1)
rsd_dT = c2t.get_distorted_dt(dT_lightcone, vel_lightcone, z, num_particles=40, los_axis=2, velocity_axis=1, periodic=False)

c2t.save_cbin(out1_box, dT_lightcone)
c2t.save_cbin(out1_pv_box, rsd_dT)
np.savetxt(file1_z,out_z,fmt="%f")

vel_lightcone, z = c2t.make_velocity_lightcone(vel_files, dens_files, z_low, z_high, los_axis=2)
dT_lightcone,out_z = c2t.make_lightcone(dT_files, z_low , z_high, cbin_bits=64, cbin_order='F', los_axis=2)
rsd_dT = c2t.get_distorted_dt(dT_lightcone, vel_lightcone, z, num_particles=40, los_axis=2, velocity_axis=2, periodic=False)

c2t.save_cbin(out2_box, dT_lightcone)
c2t.save_cbin(out2_pv_box, rsd_dT)
np.savetxt(file2_z,out_z,fmt="%f")

