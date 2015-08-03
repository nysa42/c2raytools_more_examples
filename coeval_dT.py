# PURPOSE: Program to calculate mean, rms, and skewness of dT for coeval cubes with and without
#          redshift space distortions and with and without smoothing.
# INPUT:   The dT and dT_pv box files generated from make_dTboxes.py
# OUTPUT:  Two txt files with z, nu, mean, rms, skewness, smoothed mean, smoothed rms, and
#          smoothed skewness for redshift space distortions and not
# USAGE:   Be sure to set the paths, filenames, max z, and smoothing parameters
# AUTHOR:  Keri L. Dixon 17.04.2014


import c2raytools as c2t
import numpy as np
from scipy.stats import kurtosis
import glob
import os.path

# Filenames and path
#density_path = '/research/prace/sph_smooth_cubepm_130627_12_6912_500Mpc_ext2/global/so/nc300/'
density_path = '/research/prace/sph_smooth_cubepm_130329_10_4000_244Mpc_ext2_test/global/so/nc250/'
#density_path = '/research/prace/sph_smooth_cubepm_130315_6_1728_47Mpc_ext2/nc306/'
xfrac_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2S_250/results/'
output_filename = './results/dT_b10nu147_244Mpc_8.2S_250.dat'
out2_filename = './results/dT_rsd_b10nu147_244Mpc_8.2S_250.dat'
z_filename = '../reds_full.dat'

#c2t.set_verbose(True)
c2t.set_sim_constants(boxsize_cMpc = 244.)

# Read in z file, convert to frequncy, set minimum, and set smoothing (beam and bandwidth
z_arr = np.loadtxt(z_filename)
nu = c2t.cosmology.z_to_nu(z_arr)
dnu = 1.47 #0.440, 0.293, 0.733, 1.47
beam = 10 #3, 2, 5, 10
z_min = 10

out = open(output_filename, 'w')
out2 = open(out2_filename, 'w')

#print c2t.const.rho_crit_0*c2t.const.OmegaB*(1+22)**3

# Loop over z and read in dT. Calculate away!
for i in range(z_min,len(z_arr)):
    print 'z = %.3f'% (z_arr[i])
    dT_file = ''.join(glob.glob('./dT_boxes/dT_%.3f.cbin' % (z_arr[i])))
    print 'dT file = %s' % dT_file
    dT_box = c2t.read_cbin(dT_file, bits=64, order='F')

    dT_rsd_file = ''.join(glob.glob('./dT_pv_boxes/dT_pv_%.3f.cbin' % (z_arr[i])))
    print 'Distorted dT file = %s' % dT_rsd_file
    dT_rsd_box = c2t.read_cbin(dT_rsd_file, bits=64, order='F')

    dT_mean = dT_box.mean()
    #print dT_mean
    dT_rsd_mean = dT_rsd_box.mean()
    #print dT_mean, dT_rsd_mean
    dT_rms = c2t.rootmeansquare(dT_box)
    dT_rsd_rms = c2t.rootmeansquare(dT_rsd_box)
    dT_skew = c2t.skewness(dT_box)
    dT_rsd_skew = c2t.skewness(dT_rsd_box)
    dT_kurt = kurtosis(dT_box.flatten())
    dT_rsd_kurt = kurtosis(dT_rsd_box.flatten())
    #print dT_skew, dT_rsd_kurt
    print 'z, nu, dT_mean, dT_rms %.3f %.3f %.4f %.4f %.4f' % (z_arr[i], nu[i], dT_mean, dT_rms, dT_kurt)
    #print 'z, nu, dT_mean, dT_rms %.3f %.3f %.4f %.4f' % (z_arr[i], nu[i], dT_rsd_mean, dT_rsd_rms)

    # Set the bandwidth and convert to cells
    nu_low = c2t.z_to_nu(z_arr[i]) - dnu/2
    nu_high = c2t.z_to_nu(z_arr[i]) + dnu/2
    z_low = c2t.nu_to_z(nu_high)
    z_high = c2t.nu_to_z(nu_low)
    n_cells = (c2t.z_to_cdist(z_high) - c2t.z_to_cdist(z_low))/c2t.conv.LB*len(dT_box)

    frac, width = np.modf(n_cells)
    print 'n_cells with frac and width and mesh', n_cells, frac, width, len(dT_box)
    
    k = 0
    dTconv_mean = 0
    dTconv_rms = 0
    dTconv_skew = 0
    dTconv_kurt = 0
    dTconv_rsd_mean = 0
    dTconv_rsd_rms = 0
    dTconv_rsd_skew = 0
    dTconv_rsd_kurt = 0
    count = 0
    width = int(width)

    # Add up the dT slices in the bandwidth and find mean, rms, skewness
    while (k < len(dT_box)-width-1):
        print 'k=',k
        dT_slice = frac*dT_box[k,:,:]
        dT_rsd_slice = frac*dT_rsd_box[k,:,:]
        for j in range(1,width+1):
            dT_slice += dT_box[k+j,:,:]
            dT_rsd_slice += dT_rsd_box[k+j,:,:]
        dT_slice /= n_cells
        dT_rsd_slice /= n_cells
        dTconv_slice = c2t.beam_convolve(dT_slice, z_arr[i], c2t.conv.LB, beam_w=beam)
        dTconv_rsd_slice = c2t.beam_convolve(dT_rsd_slice, z_arr[i], c2t.conv.LB, beam_w=beam)
        
        dTconv_mean += dTconv_slice.mean()
        dTconv_rsd_mean += dTconv_rsd_slice.mean()
        dTconv_rms += c2t.rootmeansquare(dTconv_slice)
        dTconv_rsd_rms += c2t.rootmeansquare(dTconv_rsd_slice)
        dTconv_skew += c2t.skewness(dTconv_slice)
        dTconv_rsd_skew += c2t.skewness(dTconv_rsd_slice)
        dTconv_kurt += kurtosis(dTconv_slice.flatten())
        dTconv_rsd_kurt += kurtosis(dTconv_rsd_slice.flatten())
        
        k += width + 1
        count += 1

    dTconv_mean /= count
    dTconv_rms /= count
    dTconv_skew /= count
    dTconv_kurt /=count
    dTconv_rsd_mean /= count
    dTconv_rsd_rms /= count
    dTconv_rsd_skew /= count
    dTconv_rsd_kurt /= count
    print dTconv_kurt, dTconv_skew, dTconv_mean
    print 'number of nu bins ', count

    print 'z, nu, dT_mean, dT_rms, dT_skew %.3f %.3f %.4f %.4f %.4f %.4f' % (z_arr[i], nu[i], dTconv_mean, dTconv_rms, dTconv_skew, dTconv_kurt)
    print 'z, nu, dT_mean, dT_rms, dT_skew %.3f %.3f %.4f %.4f %.4f %.4f' % (z_arr[i], nu[i], dTconv_rsd_mean, dTconv_rsd_rms, dTconv_rsd_skew, dTconv_rsd_kurt)
    out.write('%.3f %.3f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f\n' % (z_arr[i], nu[i], dT_mean, dT_rms, dT_skew, dT_kurt, dTconv_mean, dTconv_rms, dTconv_skew, dTconv_kurt))
    out2.write('%.3f %.3f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f\n' % (z_arr[i], nu[i], dT_rsd_mean, dT_rsd_rms, dT_rsd_skew, dT_rsd_kurt, dTconv_rsd_mean, dTconv_rsd_rms, dTconv_rsd_skew, dTconv_rsd_kurt))

out.close()
out2.close()
