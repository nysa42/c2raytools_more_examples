#This file illustrates some basic usage for the c2raytools package
#The script reads some data files and prints and plots some statistics

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator

mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['axes.labelsize'] = 17

#Some path names. Modify these as needed
one_filename = '../1244Mpc_f2_0_250_pyt/results/dT_rsd_b3nu44_244Mpc_0_250.dat'
two_filename =	'../1244Mpc_f2_8.2S_250_pyt/results/dT_rsd_b3nu44_244Mpc_8.2S_250.dat'
three_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/dT_rsd_b3nu44_244Mpc_8.2pS_250.dat'
four_filename = '../1244Mpc_f2_gS_250_pyt/results/dT_rsd_b3nu44_244Mpc_gS_250.dat'
five_filename = '../1244Mpc_f2_0_250_pyt/results/xfrac_244Mpc_f2_0_250.dat'
six_filename =	'../1244Mpc_f2_8.2S_250_pyt/results/xfrac_244Mpc_f2_8.2S_250.dat'
seven_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/xfrac_244Mpc_f2_8.2pS_250.dat'
eight_filename = '../1244Mpc_f2_gS_250_pyt/results/xfrac_244Mpc_f2_gS_250.dat'

#Read in dTx files files (z, nu, dT_mean, dTconv_mean, dTconv_rms, dTconv_skew)
f1 = np.loadtxt(one_filename)
f2 = np.loadtxt(two_filename)
f3 = np.loadtxt(three_filename)
f4 = np.loadtxt(four_filename)
f5 = np.loadtxt(five_filename)
f6 = np.loadtxt(six_filename)
f7 = np.loadtxt(seven_filename)
f8 = np.loadtxt(eight_filename)

pl.figure()
pl.plot(f1[:,1],f1[:,8],'r-',lw=1.5,label='L1')
pl.plot(f2[:,1],f2[:,8],'b:',lw=2,label='L2')
pl.plot(f3[:,1],f3[:,8],'g--',lw=2,label='L3')
pl.plot(f4[:,1],f4[:,8],'m-.',lw=2,label='L4')
#pl.plot(f1[:,1],f1[:,8],'r',label='no LMACHs')
#pl.plot(f2[:,1],f2[:,8],'b',label='supp LMACHs')
#pl.plot(f3[:,1],f3[:,8],'g',label='psupp LMACHs')
#pl.plot(f4[:,1],f4[:,8],'m',label='gsupp LMACHs')
pl.ylim([-3,8])
pl.xlim([210,70])
#pl.title('rms Source comparison with 5" beam, 0.4 MHz')
pl.xlabel('$\\nu_{\\rm obs}\, \\rm{[MHz]}$')
pl.ylabel('$\\rm skewness$')
pl.minorticks_on()
leg = pl.legend(loc='upper right',prop={'size':11})
leg.draw_frame(False)
pl.savefig('./eps/dTskew_244_rsd_b3nu44_sources.eps')
pl.savefig('./png/dTskew_244_rsd_b3nu44_sources.png')

pl.clf()
pl.plot(f5[:,2],f1[:,8],'r-',lw=1.5,label='L1')
pl.plot(f6[:,2],f2[:,8],'b:',lw=2,label='L2')
pl.plot(f7[:,2],f3[:,8],'g--',lw=2,label='L3')
pl.plot(f8[:,2],f4[:,8],'m-.',lw=2,label='L4')
#pl.plot(f5[:,2],f1[:,7],'r',label='no LMACHs')
#pl.plot(f6[:,2],f2[:,7],'b',label='supp LMACHs')
#pl.plot(f7[:,2],f3[:,7],'g',label='psupp LMACHs')
#pl.plot(f8[:,2],f4[:,7],'m',label='gsupp LMACHs')
pl.ylim([-3,8])
pl.xlim([1.05,-0.05])
#pl.title('rms source comparison with 5" beam, 0.4 MHz')
pl.xlabel('$x_{\\rm m}$')
pl.ylabel('$\\rm skewness$')
pl.minorticks_on()
leg = pl.legend(loc='upper right',prop={'size':11})
leg.draw_frame(False)
pl.savefig('./eps/dTskewxi_244_rsd_b3nu44_sources.eps')
pl.savefig('./png/dTskewxi_244_rsd_b3nu44_sources.png')

pl.clf()
fg = gridspec.GridSpec(2,1)
fg.update(hspace=0)
up = pl.subplot(fg[0, :])
up.plot(f1[:,1],f1[:,8],'r-',label='L1',lw=1.5)
up.plot(f2[:,1],f2[:,8],'b:',label='L2',lw=2)
up.plot(f3[:,1],f3[:,8],'g--',label='L3',lw=2)
up.plot(f4[:,1],f4[:,8],'m-.',label='L4',lw=2)
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
low.plot(f2[:,1],f2[:,9],'b:',label='L2',lw=2)
low.plot(f3[:,1],f3[:,9],'g--',label='L3',lw=2)
low.plot(f4[:,1],f4[:,9],'m-.',label='L4',lw=2)
low.set_ylim([-3,9])
low.set_xlim([210,70])
low.set_ylabel('$\\rm{kurtosis}$')
low.set_xlabel('$\\nu_{\\rm obs}\, \\rm{[MHz]}$')
low.minorticks_on()

pl.setp(up.get_xticklabels(), visible=False)
pl.minorticks_on()
pl.savefig('./eps/dTskewkurt_244_rsd_b3nu44_sources.eps')
pl.savefig('./png/dTskewkurt_244_rsd_b3nu44_sources.png')

pl.clf()
fg = gridspec.GridSpec(2,1)
fg.update(hspace=0)
up = pl.subplot(fg[0, :])
up.plot(f5[:,2],f1[:,8],'r-',label='L1',lw=1.5)
up.plot(f6[:,2],f2[:,8],'b:',label='L2',lw=2)
up.plot(f7[:,2],f3[:,8],'g--',label='L3',lw=2)
up.plot(f8[:,2],f4[:,8],'m-.',label='L4',lw=2)
up.set_ylabel('$\\rm skewness$')
up.set_ylim([-3,9])
up.set_xlim([1.05,-0.05])
up.minorticks_on()
up_yax = up.axes.get_yaxis() 
up_yax.set_major_locator(MaxNLocator(integer=True))
leg = up.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)
low = pl.subplot(fg[1, :])
low.plot(f5[:,2],f1[:,9],'r-',label='L1',lw=1.5)
low.plot(f6[:,2],f2[:,9],'b:',label='L2',lw=2)
low.plot(f7[:,2],f3[:,9],'g--',label='L3',lw=2)
low.plot(f8[:,2],f4[:,9],'m-.',label='L4',lw=2)
low.set_ylim([-3,9])
low.set_xlim([1.05,-0.05])
low.set_ylabel('$\\rm{kurtosis}$')
low.set_xlabel('$x_{\\rm m}$')
low.minorticks_on()

pl.setp(up.get_xticklabels(), visible=False)
pl.minorticks_on()
pl.savefig('./eps/dTskewkurtxi_244_rsd_b3nu44_sources.eps')
pl.savefig('./png/dTskewkurtxi_244_rsd_b3nu44_sources.png')


