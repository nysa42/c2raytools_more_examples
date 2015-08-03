# PURPOSE: Program to calculate the dT PDFS (distorted and not) over an entire box with beam smoothing
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
output_path = './results/dT_PDF_b3nu44_244Mpc_8.2S_250_'
out1_path = './results/dT_PDF_rsd_b3nu44_244Mpc_8.2S_250_'
out2_path = './results/dT_PDF_244Mpc_8.2S_250_'
out3_path = './results/dT_PDF_rsd_244Mpc_8.2S_250_'

z_arr = np.loadtxt(z_filename, unpack=True)

beam = 3
dnu = 0.44

c2t.set_sim_constants(boxsize_cMpc = 244.)

for i in range(1,len(z_arr)):
    output_filename = output_path+'%.3f.dat'%(z_arr[i])
    out1_filename = out1_path+'%.3f.dat'%(z_arr[i])
    out2_filename = out2_path+'%.3f.dat'%(z_arr[i])
    out3_filename = out3_path+'%.3f.dat'%(z_arr[i])
    print 'z = %.3f'% (z_arr[i])
 
    dT_file = ''.join(glob.glob('./dT_boxes/dT_%.3f.cbin'%(z_arr[i])))
    print 'dT file = %s' % dT_file
    dT_box = c2t.read_cbin(dT_file, bits=64, order='F')
    
    dT_rsd_file = ''.join(glob.glob('./dT_pv_boxes/dT_pv_%.3f.cbin'%(z_arr[i])))
    print 'dT_pv file = %s' % dT_rsd_file
    dT_rsd_box = c2t.read_cbin(dT_rsd_file, bits=64, order='F')

    dTraw_mean = dT_box.mean()
    dTraw_rsd_mean = dT_rsd_box.mean()
    dTraw_var = np.mean(pow(dT_box-dTraw_mean,2))
    dTraw_rsd_var = np.mean(pow(dT_rsd_box-dTraw_rsd_mean,2))
    
    print 'Calculating coeval dT PDFs...'

    dTraw_hist, dTraw_bin_edges = np.histogram(dT_box,bins=100,density=True)
    dTraw_rsd_hist, dTraw_rsd_bin_edges = np.histogram(dT_rsd_box,bins=100,density=True)

    dTraw_bins = np.zeros(len(dTraw_hist))
    dTraw_rsd_bins = np.zeros(len(dTraw_rsd_hist))
    out2 = open(out2_filename, 'w')
    out3 = open(out3_filename, 'w')
    
    for j in range(0,len(dTraw_hist)):
        dTraw_bins[j] = (dTraw_bin_edges[j+1] - dTraw_bin_edges[j])/2 + dTraw_bin_edges[j]
        dTraw_rsd_bins[j] = (dTraw_rsd_bin_edges[j+1] - dTraw_rsd_bin_edges[j])/2 + dTraw_rsd_bin_edges[j]

        #print 'dT_bin, dT_hist, dT_mean %.4f %.4e %.4f' % (dTraw_bins[j], dTraw_hist[j], dTraw_mean)
        #print 'dT_rsd_bin, dT_hist, dT_mean %.4f %.4e %.4f' % (dTraw_rsd_bins[j], dTraw_rsd_hist[j], dTraw_rsd_mean)
        out2.write('%.4f %.4e %.4e %.4e\n' % (dTraw_bins[j], dTraw_hist[j], dTraw_mean, dTraw_var))
        out3.write('%.4f %.4e %.4e %.4e\n' % (dTraw_rsd_bins[j], dTraw_rsd_hist[j], dTraw_rsd_mean, dTraw_rsd_var))
    
    out2.close()
    out3.close()

   # Set the bandwidth and convert to cells
    nu_low = c2t.z_to_nu(z_arr[i]) - dnu/2
    nu_high = c2t.z_to_nu(z_arr[i]) + dnu/2
    z_low = c2t.nu_to_z(nu_high)
    z_high = c2t.nu_to_z(nu_low)
    n_cells = (c2t.z_to_cdist(z_high) - c2t.z_to_cdist(z_low))/c2t.conv.LB*len(dT_box)

    frac, width = np.modf(n_cells)
    print 'n_cells with frac and width and mesh', n_cells, frac, width, len(dT_box)
    
    k = 0
    dTconv_mean = 0.
    dTconv_rsd_mean = 0.
    dTconv_var = 0.
    dTconv_rsd_var = 0.
    count = 0
    width = int(width)

    # Add up the dT slices in the bandwidth and find mean, rms, skewness
    while (k < len(dT_box)-width-1):
        #print 'k=',k
        dT_slice = frac*dT_box[k,:,:]
        dT_rsd_slice = frac*dT_rsd_box[k,:,:]
        for j in range(1,width+1):
            dT_slice += dT_box[k+j,:,:]
            dT_rsd_slice += dT_rsd_box[k+j,:,:]
        dT_slice /= n_cells
        dT_rsd_slice /= n_cells
        #print 'slices', dT_slice, dT_rsd_slice
        dTconv_slice = c2t.beam_convolve(dT_slice, z_arr[i], c2t.conv.LB, beam_w=beam)
        dTconv_rsd_slice = c2t.beam_convolve(dT_rsd_slice, z_arr[i], c2t.conv.LB, beam_w=beam)
        #print 'shapes conv', dTconv_slice, dTconv_rsd_slice

        if k == 0:
            dT_PDF_box = dTconv_slice
            dT_rsd_PDF_box = dTconv_rsd_slice
            
        elif k > 0:
            dT_PDF_box = np.dstack((dT_PDF_box,dTconv_slice))
            dT_rsd_PDF_box = np.dstack((dT_rsd_PDF_box,dTconv_rsd_slice))
            #print 'shapes ', k, dT_PDF_box.shape, dT_rsd_PDF_box.shape
            
        dTconv_mean += dTconv_slice.mean()
        dTconv_rsd_mean += dTconv_rsd_slice.mean()
        dTconv_var += np.mean(pow(dTconv_slice-dTconv_mean,2))
        dTconv_rsd_var += np.mean(pow(dTconv_rsd_slice-dTconv_rsd_mean,2))
        
        k += width + 1
        count += 1

    dTconv_mean /= count
    dTconv_rsd_mean /= count
    dTconv_var /= count
    dTconv_rsd_var /= count
    
    print 'number of nu bins ', count

    dT_hist, dT_bin_edges = np.histogram(dT_PDF_box,bins=100,density=True)
    dT_rsd_hist, dT_rsd_bin_edges = np.histogram(dT_rsd_PDF_box,bins=100,density=True)

    #print 'huh ', dT_hist, dT_bin_edges
    print 'length ', len(dT_hist), len(dT_bin_edges)

    dT_bins = np.zeros(len(dT_hist))
    dT_rsd_bins = np.zeros(len(dT_rsd_hist))
    out = open(output_filename, 'w')
    out1 = open(out1_filename, 'w')
    
    for j in range(0,len(dT_hist)):
        dT_bins[j] = (dT_bin_edges[j+1] - dT_bin_edges[j])/2 + dT_bin_edges[j]
        dT_rsd_bins[j] = (dT_rsd_bin_edges[j+1] - dT_rsd_bin_edges[j])/2 + dT_rsd_bin_edges[j]

        #print 'dT_bin, dT_hist, dT_mean %.4f %.4e %.4f' % (dT_bins[j], dT_hist[j], dTconv_mean)
        #print 'dT_rsd_bin, dT_hist, dT_mean %.4f %.4e %.4f' % (dT_rsd_bins[j], dT_rsd_hist[j], dTconv_rsd_mean)
        out.write('%.4f %.4e %.4e %.4e\n' % (dT_bins[j], dT_hist[j], dTconv_mean, dTconv_var))
        out1.write('%.4f %.4e %.4e %.4e\n' % (dT_rsd_bins[j], dT_rsd_hist[j], dTconv_rsd_mean, dTconv_rsd_var))
    
    out.close()
    out1.close()
