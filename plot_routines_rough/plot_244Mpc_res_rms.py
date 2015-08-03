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
one_filename = '../1244Mpc_f2_0_250_pyt/results/dT_rsd_b3nu44_244Mpc_0_250.dat'
two_filename =	'../1244Mpc_f2_0_500_pyt/results/good_dT_rsd_b3nu44_244Mpc_0_500.dat'
three_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/dT_rsd_b3nu44_244Mpc_8.2pS_250.dat'
four_filename = '../1244Mpc_f2_8.2pS_500_pyt/results/dT_rsd_b3nu44_244Mpc_8.2pS_500.dat'
five_filename = '../1244Mpc_f2_0_250_pyt/results/xfrac_244Mpc_f2_0_250.dat'
six_filename =	'../1244Mpc_f2_0_500_pyt/results/xfrac_244Mpc_f2_0_500.dat'
seven_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/xfrac_244Mpc_f2_8.2pS_250.dat'
eight_filename = '../1244Mpc_f2_8.2pS_500_pyt/results/xfrac_244Mpc_f2_8.2pS_500.dat'

#Read in dTx files files (z, nu, dT_mean, dTconv_mean, dTconv_rms, dTconv_skew)
f1 = np.loadtxt(one_filename)
f2 = np.loadtxt(two_filename)
f3 = np.loadtxt(three_filename)
f4 = np.loadtxt(four_filename)
f5 = np.loadtxt(five_filename)
f6 = np.loadtxt(six_filename)
f7 = np.loadtxt(seven_filename)
f8 = np.loadtxt(eight_filename)

#Plot volume and mass neutral fractions
pl.figure()
pl.plot(f5[:,2],f1[:,7],'r-',lw=1.5,label='244Mpc_0_250')
pl.plot(f6[:,2],f2[:,7],'r:',lw=2,label='244Mpc_0_500')
pl.plot(f7[:,2],f3[:,7],'g-',lw=2,label='244Mpc_8.2pS_250')
pl.plot(f8[:,2],f4[:,7],'g:',lw=2,label='244Mpc_8.2pS_500')
#pl.plot(f5[:,2],f1[:,7],'r',label='no LMACHs')
#pl.plot(f6[:,2],f2[:,7],'b',label='supp LMACHs')
#pl.plot(f7[:,2],f3[:,7],'g',label='psupp LMACHs')
#pl.plot(f8[:,2],f4[:,7],'m',label='gsupp LMACHs')
pl.ylim([0,5.5])
pl.xlim([1.05,-0.05])
#pl.title('rms source comparison with 5" beam, 0.4 MHz')
pl.xlabel('$x_{\\rm m}$')
pl.ylabel('$\langle\delta T_{\\rm b}\rangle^{1/2}\; \\rm{[mK]}$')
pl.minorticks_on()
leg = pl.legend(loc='lower right',prop={'size':11})
leg.draw_frame(False)
pl.savefig('./eps/dTrmsxi_244_rsd_b3nu44_res.eps')
pl.savefig('./png/dTrmsxi_244_rsd_b3nu44_res.png')

pl.clf()
fg = gridspec.GridSpec(1,1)
fg.update(hspace=0)
fig = pl.subplot(fg[0, :])
fig.plot(f1[:,1],f1[:,7],'r-',lw=1.5,label='244Mpc_0_250')
fig.plot(f2[:,1],f2[:,7],'r:',lw=2,label='244Mpc_0_500')
fig.plot(f3[:,1],f3[:,7],'g-',lw=1.5,label='244Mpc_8.2pS_250')
fig.plot(f4[:,1],f4[:,7],'g:',lw=2,label='244Mpc_8.2pS_500')
fig.set_ylim([0,5.65])
fig.set_xlim([210,61])
fig.set_xlabel('$\\nu_{\\rm obs}\; \\rm{[MHz]}$')
fig.set_ylabel('$<\delta T_{\\rm b}>^{1/2} \\rm{[mK]}$')
fig.minorticks_on()
leg = fig.legend(loc='upper right',prop={'size':11})
leg.draw_frame(False)
mpl.rcParams['xtick.labelsize'] = 11
mpl.rcParams['ytick.labelsize'] = 11
a = inset_axes(fig.axes, width="30%", height="30%",loc=4, borderpad=1.5) #width="30%", height="30%",add_axes([7, 4, 1, 1])
a.plot(f1[:,1],f1[:,2],'r-',lw=1.1)
a.plot(f2[:,1],f2[:,2],'r:',lw=1.5)
a.plot(f3[:,1],f3[:,2],'g-',lw=1.1)
a.plot(f4[:,1],f4[:,2],'g:',lw=1.5)
a.set_ylim([0,40])
a.set_xlim([209,69])
a.yaxis.set_ticks((0,10,20,30,40))
a.xaxis.set_ticks((200,170,140,110,80))
a.set_ylabel('$\delta T_{\\rm b} \\rm{[mK]}$')
#a.minorticks_on()
#a.xaxis.set_label_position('top') 
#a.get_xaxis().set_visible(False)
pl.savefig('./eps/dTinset_244_rsd_b3nu44_res.eps')
pl.savefig('./png/dTinset_244_rsd_b3nu44_res.png')

pl.clf()
fg = gridspec.GridSpec(2,1)
fg.update(hspace=0)
up = pl.subplot(fg[0, :])
up.plot(f1[:,1],f1[:,8],'r-',label='L1',lw=1.5)
up.plot(f2[:,1],f2[:,8],'r:',label='L1_HR',lw=2)
up.plot(f3[:,1],f3[:,8],'g-',label='L3',lw=2)
up.plot(f4[:,1],f4[:,8],'g:',label='L3_HR',lw=2)
up.set_ylabel('$\\rm skewness$')
up.set_ylim([-3,9])
up.set_xlim([210,70])
up.minorticks_on()
up_yax = up.axes.get_yaxis() 
up_yax.set_major_locator(MaxNLocator(integer=True))
leg = up.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)
low = pl.subplot(fg[1, :])
low.plot(f1[:,1],f1[:,9],'r-',label='L1',lw=1.5)
low.plot(f2[:,1],f2[:,9],'r:',label='L1_HR',lw=2)
low.plot(f3[:,1],f3[:,9],'g-',label='L3',lw=1.5)
low.plot(f4[:,1],f4[:,9],'g:',label='L3_HR',lw=2)
low.set_ylim([-3,9])
low.set_xlim([210,70])
low.set_ylabel('$\\rm{kurtosis}$')
low.set_xlabel('$\\nu_{\\rm obs}\; \\rm{[MHz]}$')
low.minorticks_on()

pl.setp(up.get_xticklabels(), visible=False)
pl.minorticks_on()
pl.savefig('./eps/dTskewkurt_244_rsd_b3nu44_res.eps')
pl.savefig('./png/dTskewkurt_244_rsd_b3nu44_res.png')

pl.clf()
fg = gridspec.GridSpec(2,1)
fg.update(hspace=0)
up = pl.subplot(fg[0, :])
up.plot(f5[:,2],f1[:,8],'r-',label='244Mpc_0_250',lw=1.5)
up.plot(f6[:,2],f2[:,8],'r:',label='244Mpc_0_500',lw=2)
up.plot(f7[:,2],f3[:,8],'g-',label='244Mpc_8.2pS_250',lw=2)
up.plot(f8[:,2],f4[:,8],'g:',label='244Mpc_8.2pS_500',lw=2)
up.set_ylabel('$\\rm skewness$')
up.set_ylim([-3,9])
up.set_xlim([1.05,-0.05])
up.minorticks_on()
up_yax = up.axes.get_yaxis() 
up_yax.set_major_locator(MaxNLocator(integer=True))
leg = up.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)
low = pl.subplot(fg[1, :])
low.plot(f5[:,2],f1[:,9],'r-',label='244Mpc_0_250',lw=1.5)
low.plot(f6[:,2],f2[:,9],'r:',label='244Mpc_0_500',lw=2)
low.plot(f7[:,2],f3[:,9],'g-',label='244Mpc_8.2pS_250',lw=2)
low.plot(f8[:,2],f4[:,9],'g:',label='244Mpc_8.2pS_500',lw=2)
low.set_ylim([-3,9])
low.set_xlim([1.05,-0.05])
low.set_ylabel('$\\rm{kurtosis}$')
low.set_xlabel('$x_{\\rm m}$')
low.minorticks_on()

pl.setp(up.get_xticklabels(), visible=False)
pl.minorticks_on()
pl.savefig('./eps/dTskewkurtxi_244_rsd_b3nu44_res.eps')
pl.savefig('./png/dTskewkurtxi_244_rsd_b3nu44_res.png')


