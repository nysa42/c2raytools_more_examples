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
#density_path = '/research/prace/sph_smooth_cubepm_130329_10_4000_244Mpc_ext2_test/global/so/nc250/'
#density_path = '/research/prace/sph_smooth_cubepm_130315_6_1728_47Mpc_ext2/nc306/'
#xfrac_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2pS_250/results/'
xfrac_path = './'
#xfrac_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2S_H250_2/results/'
output_filename = './results/meanT_244Mpc_2.dat'
fpdf_out = './results/T_PDF_244Mpc_2.dat'
z_filename = '../reds_full.dat'

# Read in z file to get snap and redshift and set mesh
#z_arr = np.loadtxt(z_filename, unpack=True, skiprows=1)
#z_arr = [12.751]
z_arr = [13.221]
z_min = 0

out = open(output_filename, 'w') # open output file
pdf_out = open(fpdf_out, 'w')

#Loop over z
for i in range(z_min,len(z_arr)):
    print 'z = %.3f'% (z_arr[i])
    #density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat'%(z_arr[i])))
    #if not density_file:
    #    density_file = ''.join(glob.glob(density_path+'%.3fn_all.dat'%(z_arr[i-1])))
    #print 'Desnity file = %s' % density_file
    #dfile = c2t.DensityFile(density_file)

    temper_file = ''.join(glob.glob(xfrac_path+'Temper3D_%.3f.bin'%(z_arr[i])))
    print 'Temperature file = %s' % temper_file
    
    tfile = c2t.TemperFile(temper_file)
   
    T_mean = tfile.temper.mean()
    T_rms = c2t.rootmeansquare(tfile.temper)
    T_var = np.mean(pow(tfile.temper-T_mean,2))
#avg_mG = c2t.mass_weighted_mean_xi(ifile.irate,dfile.raw_density)

    print 'min T = ',tfile.temper.min(),' and max T = ',tfile.temper.max()
    print 'T_CMB = ',2.725*(1+z_arr[i])
    print 'z, avg_vG, rms = %.3f %.3f %.4e' % (z_arr[i], T_mean, T_rms)
    out.write('%.3f %.4f %.4e\n' % (z_arr[i], T_mean, T_rms))

    log_bins = np.logspace(1.,5.,100)
    T_hist, T_bin_edges = np.histogram(tfile.temper,bins=log_bins,density=True)
    T_bins = np.zeros(len(T_hist))

    for j in range(0,len(T_hist)):
        T_bins[j] = (T_bin_edges[j+1] - T_bin_edges[j])/2 + T_bin_edges[j]
        pdf_out.write('%.4f %.4e %.4e %.4e\n' % (T_bins[j], T_hist[j], T_mean, T_var))
        
out.close()
pdf_out.close()
