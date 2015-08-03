# PURPOSE: Program to calculate the dT lightcone along three lines of sight with bandwidth and beam convolution
# INPUT: The dT boxes from make_dTboxes.py and a redshift file
# OUTPUT: Two txt files with z, nu, mean, rms for smoothing and not
# USAGE: Be sure to set the paths, names, smoothing, and mesh appropriately
# AUTHOR: Keri L. Dixon 21.04.2014


import c2raytools as c2t
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import glob
import os.path
from matplotlib.ticker import MaxNLocator, MultipleLocator
from matplotlib.colors import LogNorm

mpl.rcParams['axes.labelsize'] = 17

#Filenames and path
cbin1_file = '../1244Mpc_f2_0_250_pyt/lc_pic_boxes/dT_lc1_244Mpc_0_250.cbin'
cbin2_file = '../1244Mpc_f2_8.2S_250_pyt/lc_pic_boxes/dT_lc1_244Mpc_8.2S_250.cbin'
cbin3_file = '../1244Mpc_f2_8.2S_250_pyt/lc_pic_boxes/dT_lc1_244Mpc_8.2S_250.cbin'
cbin4_file = '../1244Mpc_f2_8.2S_250_pyt/lc_pic_boxes/dT_lc1_244Mpc_8.2S_250.cbin'

out_rawfig = './figs/lc_raw_244Mpc_f2_8.2S_250.eps'
out_pv_rawfig = './figs/lc_pv_raw_244Mpc_f2_8.2S_250.eps'
out_all_zfig = './figs/lc_z_244Mpc_all.eps'
out_beam_nufig = './figs/lc_b3nu44_244Mpc_f2_0_250.eps'
out_all_beam_nufig = './figs/lc_b3nu44_244Mpc_all.eps'

z_filename = '../1244Mpc_f2_8.2S_250_pyt/lc_pic_boxes/out0_z.dat'

c2t.set_sim_constants(boxsize_cMpc = 244.)

# Read in z file, set smoothing, and open output files
z_arr = np.loadtxt(z_filename)
nu = c2t.cosmology.z_to_nu(z_arr)[::-1]
dnu = 0.44
beam = 3.
mesh = 250

# Read in lightcones
cbin1 = c2t.read_cbin(cbin1_file)  
cbin2 = c2t.read_cbin(cbin2_file)
cbin3 = c2t.read_cbin(cbin3_file)
cbin4 = c2t.read_cbin(cbin4_file)

cb_ticks=[0,10,20,30,40,50,60,70]

xtick_zlabels = np.arange(int(np.floor(z_arr.min())),int(np.ceil(z_arr.max())),2)
xtick_zlocs = []
j = 0
for i in range(1,len(z_arr)):
    if j >= len(xtick_zlabels): break
    if (abs(xtick_zlabels[j] - z_arr[i-1]) > abs(xtick_zlabels[j] - z_arr[i])): continue
    else:
        xtick_zlocs.append(i-1)
        j += 1
print xtick_zlocs
print xtick_zlabels

print nu.min(), nu.max()
xtick_nulabels = np.arange(int(np.floor(nu.min())+4),int(np.floor(nu.max())-2),15)
print xtick_nulabels
xtick_nulocs = []
j = 0
for i in range(1,len(nu)):
    if j >= len(xtick_nulabels): break
    if (abs(xtick_nulabels[j] - nu[i-1]) > abs(xtick_nulabels[j] - nu[i])): continue
    else:
        xtick_nulocs.append(i-1)
        j += 1
xtick_nulabels = xtick_nulabels[::-1]
print xtick_nulabels
print xtick_nulocs

ytick_labels = [15,110,205,300]
ytick_locs = [15/c2t.conv.LB*mesh, 110/c2t.conv.LB*mesh, 205/c2t.conv.LB*mesh, 300/c2t.conv.LB*mesh]
#ytick_locs = ytick_labels*mesh/c2t.conv.LB
print ytick_locs
 
pl.figure()
fig,ax = pl.subplots()
cax = ax.imshow(cbin1[125,:,:], extent=[z_arr.max(),z_arr.min(), 0, c2t.conv.LB], cmap=mpl.cm.RdBu, vmin=0, vmax=50, origin='lower',aspect='auto')
yax = ax.axes.get_yaxis()
yax.set_major_locator(MultipleLocator(100))
pl.xticks(xtick_zlocs, xtick_zlabels)
fig.savefig(out_rawfig, bbox_inches='tight')
'''
pl.clf()
fig,ax = pl.subplots()
cax = ax.imshow(cbin2[125,:,:], cmap=mpl.cm.RdBu, vmin=0., vmax=50, origin='lower')
yax = ax.axes.get_yaxis()
yax.set_major_locator(MultipleLocator(100))
pl.xticks(xtick_nulocs, xtick_nulabels)
fig.savefig(out_pv_rawfig, bbox_inches='tight')'''

pl.clf()
fig, (ax1,ax2,ax3,ax4) = pl.subplots(4,sharex=True) # share the x axis
ax1.set_title('$\delta T_{\\rm b}\; \\rm{[mK]}$')
cax1 = ax1.imshow(cbin1[125,:,:], cmap=mpl.cm.RdBu, vmin=0, vmax=50, origin='lower')
ax1.set_yticks(ytick_locs)
ax1.set_yticklabels(ytick_labels)
ax1.set_adjustable('box-forced')
cax2 = ax2.imshow(cbin2[125,:,:], cmap=mpl.cm.RdBu, vmin=0, vmax=50, origin='lower')
ax2.set_yticks(ytick_locs)
ax2.set_yticklabels(ytick_labels)
ax2.set_adjustable('box-forced')
cax3 = ax3.imshow(cbin3[125,:,:], cmap=mpl.cm.RdBu, vmin=0, vmax=50, origin='lower')
ax3.set_yticks(ytick_locs)
ax3.set_yticklabels(ytick_labels)
ax3.set_adjustable('box-forced')
cax4 = ax4.imshow(cbin4[125,:,:], cmap=mpl.cm.RdBu, vmin=0, vmax=50, origin='lower')
ax4.set_yticks(ytick_locs)
ax4.set_yticklabels(ytick_labels)
ax4.set_adjustable('box-forced')
pl.xticks(xtick_zlocs, xtick_zlabels)

#fig.subplots_adjust(right=0.7) # moves colorbar to the right 
#cbar_ax = fig.add_axes([0.7, 0.1, 0.02, 0.8])
#fig.colorbar(cax4, cax=cbar_ax)
ax4.set_xlabel('$z$')
ax1.set_ylabel('$\\rm{L1}$')
ax2.set_ylabel('$\\rm{L2}$')
ax3.set_ylabel('$\\rm{L3}$')
ax4.set_ylabel('$\\rm{L4}$')
#fig.subplots_adjust(right=0.7) # moves colorbar to the right 
cbar_ax = fig.add_axes([0.9005, 0.215, 0.02, 0.5702])
fig.colorbar(cax4, cax=cbar_ax)
#fig.tight_layout()
fig.subplots_adjust(hspace=-0.62) # removies white space between plots
#pl.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)
fig.savefig(out_all_zfig, bbox_inches='tight')

'''
# Set blank slices and set initial bins
#nu_curr = c2t.cosmology.z_to_nu(z_arr[i]) + dnu/2
#z_curr = c2t.cosmology.nu_to_z(nu_curr)
z_low = z_arr[0]
high_z = z_arr[-1]

i = 0
dT_beam1 = np.zeros(shape=(mesh,mesh))
round = 1

# Cycle through redshifts 
while (z_low < high_z-0.05):
    nu_low = c2t.cosmology.z_to_nu(z_low)-dnu
    nu_high = c2t.cosmology.z_to_nu(z_low)
    z_high = c2t.cosmology.nu_to_z(nu_low)

    dTconv_slice1 = np.zeros(shape=(mesh,mesh))
     
    j = 0
    while(z_arr[i] < z_high):
        dTconv_slice1 += cbin1[:,:,i]
        
        i += 1
        j += 1
    frac = z_high - z_arr[i-1]
    dTconv_slice1 += frac*cbin1[:,:,i]
    dTconv_slice1 /= j + frac
    
    dT_slice1 = c2t.beam_convolve(dTconv_slice1, z_arr[i], c2t.conv.LB, beam_w=beam)
    dT_sub_slice1 = dT_slice1 - dT_slice1.mean()
    print dT_slice1.min(), dT_slice1.max()
    z_curr = (z_high - z_low)/2 + z_low
        
    if round > 0:
        dT_beam1 = dT_slice1
        dT_sub_beam1 = dT_sub_slice1
        z_beam = z_curr
        round = -1
    else:
        dT_beam1 = np.dstack((dT_beam1, dT_slice1))
        dT_sub_beam1 = np.dstack((dT_sub_beam1, dT_sub_slice1))
        z_beam = np.append(z_beam, z_curr)
        #print dT_beam.shape
        #print z_beam
    
    i += 1
    z_low = z_high

i = 0
dT_beam2 = np.zeros(shape=(mesh,mesh))
z_low = z_arr[0]
round = 1

# Cycle through redshifts 
while (z_low < high_z-0.05):
    nu_low = c2t.cosmology.z_to_nu(z_low)-dnu
    nu_high = c2t.cosmology.z_to_nu(z_low)
    z_high = c2t.cosmology.nu_to_z(nu_low)

    dTconv_slice2 = np.zeros(shape=(mesh,mesh))
     
    j = 0
    while(z_arr[i] < z_high):
        dTconv_slice2 += cbin2[:,:,i]
        
        i += 1
        j += 1
    frac = z_high - z_arr[i-1]
    dTconv_slice2 += frac*cbin2[:,:,i]
    dTconv_slice2 /= j + frac
    
    dT_slice2 = c2t.beam_convolve(dTconv_slice2, z_arr[i], c2t.conv.LB, beam_w=beam)
    dT_sub_slice2 = dT_slice2 - dT_slice2.mean()
    print dT_slice2.min(), dT_slice2.max()
    z_curr = (z_high - z_low)/2 + z_low
        
    if round > 0:
        dT_beam2 = dT_slice2
        dT_sub_beam2 = dT_sub_slice2
        z_beam = z_curr
        round = -1
    else:
        dT_beam2 = np.dstack((dT_beam2, dT_slice2))
        dT_sub_beam2 = np.dstack((dT_sub_beam2, dT_sub_slice2))
        z_beam = np.append(z_beam, z_curr)
        #print dT_beam.shape
        #print z_beam
    
    i += 1
    z_low = z_high
i = 0
dT_beam3 = np.zeros(shape=(mesh,mesh))
z_low = z_arr[0]
round = 1

# Cycle through redshifts 
while (z_low < high_z-0.05):
    nu_low = c2t.cosmology.z_to_nu(z_low)-dnu
    nu_high = c2t.cosmology.z_to_nu(z_low)
    z_high = c2t.cosmology.nu_to_z(nu_low)

    dTconv_slice3 = np.zeros(shape=(mesh,mesh))
     
    j = 0
    while(z_arr[i] < z_high):
        dTconv_slice3 += cbin3[:,:,i]
        
        i += 1
        j += 1
    frac = z_high - z_arr[i-1]
    dTconv_slice3 += frac*cbin3[:,:,i]
    dTconv_slice3 /= j + frac
    
    dT_slice3 = c2t.beam_convolve(dTconv_slice3, z_arr[i], c2t.conv.LB, beam_w=beam)
    dT_sub_slice3 = dT_slice3 - dT_slice3.mean()
    print dT_slice3.min(), dT_slice3.max()
    z_curr = (z_high - z_low)/2 + z_low
        
    if round > 0:
        dT_beam3 = dT_slice3
        dT_sub_beam3 = dT_sub_slice3
        z_beam = z_curr
        round = -1
    else:
        dT_beam3 = np.dstack((dT_beam3, dT_slice3))
        dT_sub_beam3 = np.dstack((dT_sub_beam3, dT_sub_slice3))
        z_beam = np.append(z_beam, z_curr)
        #print dT_beam.shape
        #print z_beam
    
    i += 1
    z_low = z_high
i = 0
dT_beam4 = np.zeros(shape=(mesh,mesh))
z_low = z_arr[0]
round = 1

# Cycle through redshifts 
while (z_low < high_z-0.05):
    nu_low = c2t.cosmology.z_to_nu(z_low)-dnu
    nu_high = c2t.cosmology.z_to_nu(z_low)
    z_high = c2t.cosmology.nu_to_z(nu_low)

    dTconv_slice4 = np.zeros(shape=(mesh,mesh))
     
    j = 0
    while(z_arr[i] < z_high):
        dTconv_slice4 += cbin4[:,:,i]
        
        i += 1
        j += 1
    frac = z_high - z_arr[i-1]
    dTconv_slice4 += frac*cbin4[:,:,i]
    dTconv_slice4 /= j + frac
    
    dT_slice4 = c2t.beam_convolve(dTconv_slice4, z_arr[i], c2t.conv.LB, beam_w=beam)
    dT_sub_slice4 = dT_slice4 - dT_slice4.mean()
    print dT_slice4.min(), dT_slice4.max()
    z_curr = (z_high - z_low)/2 + z_low
        
    if round > 0:
        dT_beam4 = dT_slice4
        dT_sub_beam4 = dT_sub_slice4
        z_beam = z_curr
        round = -1
    else:
        dT_beam4 = np.dstack((dT_beam4, dT_slice4))
        dT_sub_beam4 = np.dstack((dT_sub_beam4, dT_sub_slice4))
        z_beam = np.append(z_beam, z_curr)
        #print dT_beam.shape
        #print z_beam
    
    i += 1
    z_low = z_high
    
nu_beam = c2t.cosmology.z_to_nu(z_beam)
#print dT_beam.min(), dT_beam.max(), dT_sub_beam.min(), dT_sub_beam.max()

#print (c2t.z_to_cdist(z_beam.min()) - c2t.z_to_cdist(z_beam.max()))
cb_ticks=[0,5,10,15,20,25,30,35]
pl.clf()
fig,ax = pl.subplots()
cax = ax.imshow(dT_beam1[125,:,:], extent=[nu_beam.max(),nu_beam.min(), 0, c2t.conv.LB], aspect='0.055', cmap=mpl.cm.gnuplot2, vmin=0, vmax=33)
cbar = fig.colorbar(cax, shrink=0.32,pad=0,ticks=cb_ticks)
cbar.ax.set_yticklabels(cb_ticks)
ax.set_xlabel('$\\nu$ (MHz)')
ax.set_ylabel('x (Mpc)')
yax = ax.axes.get_yaxis()
yax.set_major_locator(MultipleLocator(100))
fig.savefig(out_beam_nufig, bbox_inches='tight')

pl.clf()
fig, (ax1,ax2,ax3,ax4) = pl.subplots(4,sharex=True)
cax1 = ax1.imshow(dT_beam1[125,:,:], extent=[nu_beam.max(),nu_beam.min(), 0, c2t.conv.LB], aspect='0.055', cmap=mpl.cm.RdBu, vmin=0, vmax=35)
cax2 = ax2.imshow(dT_beam2[125,:,:], extent=[nu_beam.max(),nu_beam.min(), 0, c2t.conv.LB], aspect='0.055', cmap=mpl.cm.RdBu, vmin=0, vmax=35)
cax3 = ax3.imshow(dT_beam3[125,:,:], extent=[nu_beam.max(),nu_beam.min(), 0, c2t.conv.LB], aspect='0.055', cmap=mpl.cm.RdBu, vmin=0, vmax=35)
cax4 = ax4.imshow(dT_beam4[125,:,:], extent=[nu_beam.max(),nu_beam.min(), 0, c2t.conv.LB], aspect='0.055', cmap=mpl.cm.RdBu, vmin=0, vmax=35)
fig.subplots_adjust(right=0.7)
cbar_ax = fig.add_axes([0.7, 0.1, 0.02, 0.8])
fig.colorbar(cax4, cax=cbar_ax)
ax4.set_xlabel('$\\nu \; \\rm{[Hz]}$')
ax1.set_ylabel('$\\rm{HMACH}$')
ax2.set_ylabel('$\\rm{supp}$')
ax3.set_ylabel('$\\rm{p\_supp}$')
ax4.set_ylabel('$\\rm{g\_supp}$')
fig.subplots_adjust(hspace=0)
#pl.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)
fig.savefig(out_all_beam_nufig, bbox_inches='tight')

'''
