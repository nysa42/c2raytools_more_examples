import c2raytools as c2t
import numpy as np
import glob
import os.path

# Filenames and path
#density_path = '/research/prace/sph_smooth_cubepm_130627_12_6912_500Mpc_ext2/global/so/nc300/'
used_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2S_250/sources/'
#density_path = '/research/prace/sph_smooth_cubepm_130315_6_1728_47Mpc_ext2/nc306/'
source_path = '/mnt/lustre/scratch/kd242/subgrid_sources_244Mpc/250grids/'
#source_path = '/research/prace/244Mpc_RT/subgrid_sources/250grid/'
output_filename = './results/flux_244Mpc_f2_8.2S_250.dat'
z_filename = '../red.dat'

# Read in z file to get snap and redshift and set mesh
z_arr = np.loadtxt(z_filename)
z_min = 8
SrcCol = 6 # Depends on source model
eff_L = 2.
eff_S = 8.2

c2t.set_sim_constants(boxsize_cMpc = 244.)
f_conv = c2t.conv.M_grid*c2t.const.OmegaB/c2t.const.Omega0/c2t.const.m_p

out = open(output_filename, 'w')

# Loop over z
for i in range(z_min,len(z_arr)):
    print 'z = %.3f'% (z_arr[i])
    #source_file = ''.join(glob.glob(source_path+'%.3f-coarsest_wsubgrid_gradual_sources.dat' % (z_arr[i])))
    source_file = ''.join(glob.glob(source_path+'%.3f-coarsest_wsubgrid_sources.dat' % (z_arr[i])))
    print 'Source file = %s' % source_file

    #unsupp = np.loadtxt(source_file, skiprows=1)
    #print unsupp[:,0],unsupp[:,1],unsupp[:,2],unsupp[:,3],unsupp[:,4]
    with open(source_file) as sfile:
        NumSrc = np.int(sfile.readline())
        unsupp = np.array(sfile.read().split()).reshape(NumSrc,SrcCol)
    print 'Number of unsuppressed sources ', NumSrc

    used_file = ''.join(glob.glob(used_path+'%.3f-coarsest_sources_used_wfgamma.dat' % (z_arr[i])))
    print 'Used sources file = %s' % used_file
    
    with open(used_file) as ufile:
        NumSrc_used = np.int(ufile.readline())
        supp = np.array(ufile.read().split(),dtype=float).reshape(NumSrc_used,4)
    print 'Number of used sources ', NumSrc_used
    
    #source_L = np.zeros(NumSrc)
    #source_S = np.zeros(NumSrc)
    UnsuppFlux = 0.
    for j in range(0,NumSrc):
        UnsuppFlux += np.float(unsupp[j,3])*eff_L + np.float(unsupp[j,4])*eff_S
    UnsuppFlux *= f_conv
    print UnsuppFlux

    UsedFlux = 0.
    for j in range(0,NumSrc_used):
        UsedFlux += np.long(supp[j,3])
    UsedFlux *= f_conv
    print UsedFlux
    #print 'z, avg_nHII, avg_mHII = %.3f %.4e %.4e' % (z_arr[i], avg_nHII, avg_mHII)
    #M_L = np.float(unsupp[:,3])
    #M_S = unsupp[:,4]
    #M_used = supp[:,3]
    #print M_L.shape()
    #print M_L
    #UnsuppFlux = (np.sum(M_L)*eff_L + np.sum(M_S)*eff_S)*f_conv
    #UsedFlux = np.sum(M_used)*f_conv

    print 'Unsupp and supp flux ', UnsuppFlux, UsedFlux
    out.write('%.3f %i %i %.4e %.4e \n' % (z_arr[i], NumSrc, NumSrc_used, UnsuppFlux, UsedFlux))

out.close()
