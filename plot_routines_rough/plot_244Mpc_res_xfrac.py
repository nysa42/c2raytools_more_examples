#This file illustrates some basic usage for the c2raytools package
#The script reads some data files and prints and plots some statistics

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator, MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['axes.labelsize'] = 17

#Some path names. Modify these as needed
one_filename = '../1244Mpc_f2_0_250_pyt/results/xfrac_244Mpc_f2_0_250.dat'
two_filename =	'../1244Mpc_f2_0_500_pyt/results/xfrac_244Mpc_f2_0_500.dat'
three_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/xfrac_244Mpc_f2_8.2pS_250.dat'
four_filename = '../1244Mpc_f2_8.2pS_500_pyt/results/xfrac_244Mpc_f2_8.2pS_500.dat'

#Read in xfrac files
f1 = np.loadtxt(one_filename)
f2 = np.loadtxt(two_filename)
f3 = np.loadtxt(three_filename)
f4 = np.loadtxt(four_filename)

#Plot volume and mass neutral fractions
pl.figure()
pl.plot(f1[:,0],f1[:,2],'r',label='244Mpc_f2_0_250')
pl.plot(f2[:,0],f2[:,2],'r:',label='244Mpc_f2_0_500')
pl.plot(f3[:,0],f3[:,2],'g',label='244Mpc_f2_8.2pS_250')
pl.plot(f4[:,0],f4[:,2],'g:',label='244Mpc_f2_8.2pS_500')
pl.xlim([6,18])
pl.ylim([0,1.02])
#pl.title('Mass-weighted')
pl.xlabel('$z$',fontsize=16)
pl.ylabel('$x_m$',fontsize=16)
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./pres/xfrac_244Mpc_res_mass.png')

pl.clf()
fg = gridspec.GridSpec(2,1)
fg.update(hspace=0)
up = pl.subplot(fg[0, :])
#up.plot(f1[:,0],f1[:,2]/f1[:,1],'r')
#up.plot(f2[:,0],f2[:,2]/f2[:,1],'b')
#up.plot(f3[:,0],f3[:,2]/f3[:,1],'g')
#up.plot(f4[:,0],f4[:,2]/f4[:,1],'m')
up.plot(f1[:,0],1-f1[:,1],'r-',lw=1.5)
up.plot(f2[:,0],1-f2[:,1],'r:',lw=2)
up.plot(f3[:,0],1-f3[:,1],'g-',lw=2)
up.plot(f4[:,0],1-f4[:,1],'g:',lw=2)
up.set_ylabel('$x^{\\rm v}_{\\rm HI}$')
up.set_ylim([1e-2,1.])
up.set_xlim([5.8,13])
up.minorticks_on()
#up_yax = up.axes.get_yaxis() 
#up_yax.set_major_locator(MaxNLocator(integer=True))
up.axes.get_xaxis().set_ticklabels([])
#up_xax.set_minor_locator(MultipleLocator(0.5))
#low = pl.subplot2grid((5,1),(1,0), rowspan=4, sharex=up)
low = pl.subplot(fg[1, :])
#low.plot(f1[:,0],np.log10(f1[:,2]),'r',label='no LMACHs')
#low.plot(f2[:,0],np.log10(f2[:,2]),'b',label='supp LMACHs')
#low.plot(f3[:,0],np.log10(f3[:,2]),'g',label='psupp LMACHs')
#low.plot(f4[:,0],np.log10(f4[:,2]),'m',label='gsupp LMACHs')
low.semilogy(f1[:,0],1-f1[:,2],'r-',label='244Mpc_f2_0_250',lw=1.5)
low.semilogy(f2[:,0],1-f2[:,2],'r:',label='244Mpc_f2_0_500',lw=2)
low.semilogy(f3[:,0],1-f3[:,2],'g-',label='244Mpc_f2_8.2pS_250',lw=1.5)
low.semilogy(f4[:,0],1-f4[:,2],'g:',label='244Mpc_f2_8.2pS_500',lw=2)
low.set_ylim([6e-5,1e-2])
low.set_xlim([5.8,13])
low.set_ylabel('$x^{\\rm v}_{\\rm HI}$')
low.set_xlabel('$z$')
low.minorticks_on()
mpl.rcParams['xtick.labelsize'] = 11
mpl.rcParams['ytick.labelsize'] = 11

pl.savefig('./eps/xv_244Mpc_res.eps')
pl.savefig('./png/xv_244Mpc_res.png')
#pl.savefig('./pres/xfrac_244Mpc_250_comb.png')
