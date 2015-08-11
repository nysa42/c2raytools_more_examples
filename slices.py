# PURPOSE: Program to produce ionized fraction slices
# INPUT: The ionized fraction and density files in cubep3m format and the interesting redshifts, red_short.dat 
# OUTPUT: A *.png image
# USAGE: Change density_path, xfrac_path, z_filename, and z_min to suit the simulation, and be sure to specify the slice and put in output name
# AUTHOR: Keri L. Dixon 01.07.2015

import c2raytools as c2t
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import glob
import os.path
from matplotlib.colors import LogNorm
#import numpy as np

# Set path and file names
#density_path = '/research/prace/sph_smooth_cubepm_130627_12_6912_500Mpc_ext2/global/so/nc300/'
density_path = '/research/prace/sph_smooth_cubepm_130329_10_4000_244Mpc_ext2_test/global/so/nc250/'
#density_path = '/research/prace/sph_smooth_cubepm_130315_6_1728_47Mpc_ext2/nc306/'
xfrac_path = '/research/prace/244Mpc_RT/244Mpc_f2_8.2pS_250/results/'
z_filename = 'red_short.dat'
z_full = '../reds_full.dat'
output_path = './images/xy125_ion_244Mpc_8.2pS_250_'
out1_path = './images/xy125_dens_244Mpc_8.2pS_250_'

z_arr = np.loadtxt(z_filename, unpack=True)
z_f = np.loadtxt(z_full, unpack=True, skiprows=1)

c2t.set_sim_constants(boxsize_cMpc = 244.)

mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14

my_cmap = mpl.cm.jet # get a copy of the gray color map    
my_cmap.set_under(color="white",alpha="0.5")

fig = pl.figure(frameon=False)
for i in range(len(z_arr)):
    output_filename = output_path+'%.3f.ps'%(z_arr[i])
    out1_filename = out1_path+'%.3f.ps'%(z_arr[i])
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

    dens_slice = dfile.raw_density[:,:,125]
    #dens_slice = (dens_slice - dens_slice.min())/(dens_slice.max() - dens_slice.min())
    #print 'for z = ', z_arr[i], ' min = ',dens_slice.min(),' and max = ',dens_slice.max()
    d_min = 0.
    d_max = 1.5e4
    dens_slice = (dens_slice - d_min)/(d_max - d_min)
#dens_slice = np.log10(dens_slice)

    ion_slice = xfile.xi[:,:,125]

    pl.clf()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_axis_off()
    fig.set_size_inches([5,5])

    print 'min dens and max dens = ',dfile.raw_density.min(), dfile.raw_density.max()
    #im = ax.imshow(xfile.xi[:,:,125]-xfile.xi.mean(),cmap='jet')
    im = ax.imshow(dens_slice,cmap='RdBu_r',norm=LogNorm(),alpha=1.)#vmin=0., vmax = 1.5e5))#,alpha=0.7)
    #im = ax.imshow(xfile.xi[:,:,125]-xfile.xi.mean(),cmap=my_cmap,alpha=0.5, vmin=1e-3, vmax = 0.8)
    im = ax.imshow(ion_slice,cmap='RdBu_r',norm=LogNorm(),alpha=0.35)

    pl.savefig(output_filename, bbox_inches='tight',pad_inches=0)

    #pl.clf()
    #im = ax.imshow(xfile.xi[:,:,125],cmap='winter')
    #pl.savefig(out1_filename)
