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
two_filename =	'../1244Mpc_f2_8.2S_250_pyt/results/xfrac_244Mpc_f2_8.2S_250.dat'
three_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/xfrac_244Mpc_f2_8.2pS_250.dat'
four_filename = '../1244Mpc_f2_gS_250_pyt/results/xfrac_244Mpc_f2_gS_250.dat'

#Read in xfrac files
f1 = np.loadtxt(one_filename)
f2 = np.loadtxt(two_filename)
f3 = np.loadtxt(three_filename)
f4 = np.loadtxt(four_filename)

# Data points
fan_z1 = 6.1       # Fan et al 2006 (lower limit)
fan_x1 = 4.1e-4
fan_l1 = 3.e-4
fan_z2 = 5.85
fan_x2 = 1.1e-4
fan_l2 = 3.e-5
McGr_z1 = 6.1      # McGreer et al 2011 (upper limit)
McGr_x1 = 0.5
McGr_z2 = 5.9      # McGreer et al 2015 (upper limit)
McGr_x2 = 0.06
McGr_u2 = 0.05
McGr_l2 = 0.05
Schr_z1 = 6.2      # Schroeder et al 2013 (lower limit)
Schr_x1 = 0.1
McQu_z1 = 6.3      # McQuinn et al 2008 (upper limit)
McQu_x1 = 0.5
Chor_z1 = 5.91     # Chornock et al 2013 (upper limit)
Chor_x1 = 0.11
Ota_z1 = 7.        # Ota et al 2008
Ota_u1 = 0.64
Ota_l1 = 0.32
Ota_x1 = 0.48
Ouch_z1 = 6.6      # Ouchi et al 2010 (upper limit)
Ouch_x1 = 0.2
Ouch_ul = 0.2
Ouch_z2 = 6.6      # Ouchi et al 2010 (upper limit) clustering
Ouch_x2 = 0.5


#Plot volume and mass neutral fractions
pl.figure()
#pl.plot(f1[:,0],f1[:,2],'r-', lw=1.5, label='L1')
#pl.plot(f2[:,0],f2[:,2],'b:', lw=2, label='L2')
#pl.plot(f3[:,0],f3[:,2],'g--', lw=2,label='L3')
#pl.plot(f4[:,0],f4[:,2],'m-.', lw=2, label='L4')
pl.plot(f1[:,0],f1[:,2],'r-', lw=1.5)
pl.plot(f2[:,0],f2[:,2],'b:', lw=2)
pl.plot(f3[:,0],f3[:,2],'g--', lw=2)
pl.plot(f4[:,0],f4[:,2],'m-.', lw=2)
pl.errorbar(McGr_z1,McGr_x1,0.1,uplims=True)
pl.xlim([5.7,18])
pl.ylim([0,1.02])
#pl.title('Mass-weighted')
pl.xlabel('$z$',fontsize=16)
pl.ylabel('$x_{\\rm m}$',fontsize=16)
#leg = pl.legend(loc='upper right',prop={'size':12})
#leg.draw_frame(False)
pl.savefig('./png/xfrac_244Mpc_250_mass.png')
pl.savefig('./eps/xfrac_244Mpc_250_mass.eps')

print McGr_z1,McGr_x1
pl.clf()
#fg = gridspec.GridSpec(2,1)
#fg.update(hspace=0)
#up = pl.subplot(fg[0, :])
#up.plot(f1[:,0],f1[:,2]/f1[:,1],'r')
#up.plot(f2[:,0],f2[:,2]/f2[:,1],'b')
#up.plot(f3[:,0],f3[:,2]/f3[:,1],'g')
#up.plot(f4[:,0],f4[:,2]/f4[:,1],'m')
pl.plot(f1[:,0],1-f1[:,1],'r-',lw=1.5)
pl.plot(f2[:,0],1-f2[:,1],'b:',lw=2)
pl.plot(f3[:,0],1-f3[:,1],'g--',lw=2)
pl.plot(f4[:,0],1-f4[:,1],'m-.',lw=2)
pl.errorbar(fan_z1,fan_x1,0.05,uplims=True,marker='s', color='r',label='Lya forest transmission')
pl.errorbar(fan_z2,fan_x2,0.05,uplims=True,marker='s', color='r')
pl.errorbar(McGr_z1,McGr_x1,0.05,lolims=True,marker='^', color='g',label='Dark Lya pixels')
pl.errorbar(McGr_z2,McGr_x2,0.05,lolims=True,marker='^', color='g')
pl.errorbar(Schr_z1,Schr_x1,0.05,uplims=True,marker='o', color='b',label='Quasar near zones')
pl.errorbar(McQu_z1,McQu_x1,0.05,lolims=True,marker='D', color='m',label='GRB damping wing')
pl.errorbar(Chor_z1,Chor_x1,0.05,lolims=True,marker='D', color='m')
pl.errorbar(Ota_z1,Ota_x1,0.22,0.,marker='h', color='c',label='Lya emitters')
pl.errorbar(Ouch_z1,Ouch_x1,0.05,lolims=True,marker='h', color='c')
pl.errorbar(Ouch_z2,Ouch_x2,0.05,lolims=True,marker='p', color='orange',label='Lya clustering')
pl.ylabel('$x^{\\rm v}_{\\rm HI}$')
pl.ylim([-0.06,1.])
pl.xlim([5.7,13])
pl.minorticks_on()
leg = pl.legend(loc='lower right',prop={'size':12})
leg.draw_frame(False)
#up_yax = up.axes.get_yaxis() 
#up_yax.set_major_locator(MaxNLocator(integer=True))
#up.axes.get_xaxis().set_ticklabels([])
#up_xax.set_minor_locator(MultipleLocator(0.5))
#low = pl.subplot2grid((5,1),(1,0), rowspan=4, sharex=up)
#low = pl.subplot(fg[1, :])
#low.plot(f1[:,0],np.log10(f1[:,2]),'r',label='no LMACHs')
#low.plot(f2[:,0],np.log10(f2[:,2]),'b',label='supp LMACHs')
#low.plot(f3[:,0],np.log10(f3[:,2]),'g',label='psupp LMACHs')
#low.plot(f4[:,0],np.log10(f4[:,2]),'m',label='gsupp LMACHs')
#low.semilogy(f1[:,0],1-f1[:,2],'r-',label='L1',lw=1.5)
#low.semilogy(f2[:,0],1-f2[:,2],'b:',label='L2',lw=2)
#low.semilogy(f3[:,0],1-f3[:,2],'g--',label='L3',lw=2)
#low.semilogy(f4[:,0],1-f4[:,2],'m-.',label='L4',lw=2)
#low.set_ylim([6e-5,1e-2])
#low.set_xlim([5.7,13])
#low.set_ylabel('$x^{\\rm v}_{\\rm HI}$')
#low.set_xlabel('$z$')
#low.minorticks_on()
mpl.rcParams['xtick.labelsize'] = 11
mpl.rcParams['ytick.labelsize'] = 11

pl.savefig('./eps/xv_244Mpc_250.eps')
pl.savefig('./png/xv_244Mpc_250.png')
#pl.savefig('./pres/xfrac_244Mpc_250_comb.png')
