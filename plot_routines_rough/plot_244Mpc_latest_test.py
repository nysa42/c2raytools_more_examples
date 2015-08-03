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
one_filename = '../244Mpc_f2_0_250_pyt/results/dT_rsd_b5nu4_244Mpc_0_250.dat_latest'
two_filename =	'../244Mpc_f2_8.2S_250_pyt/results/dT_rsd_b3nu2_244Mpc_8.2S_250.dat'
three_filename = '../244Mpc_f2_8.2pS_250_pyt/results/dT_rsd_b5nu4_244Mpc_8.2pS_250.dat_latest'
four_filename = '../244Mpc_f2_gS_250_pyt/results/dT_rsd_b5nu4_244Mpc_gS_250.dat'
five_filename = '../244Mpc_f2_0_250_pyt/results/xfrac_244Mpc_f2_0_250.dat'
six_filename =	'../244Mpc_f2_8.2S_250_pyt/results/xfrac_244Mpc_f2_8.2S_250.dat'
seven_filename = '../244Mpc_f2_8.2pS_250_pyt/results/xfrac_244Mpc_f2_8.2pS_250.dat'
eight_filename = '../244Mpc_f2_gS_250_pyt/results/xfrac_244Mpc_f2_gS_250.dat'

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
pl.plot(f1[:,1],f1[:,3],'r-',label='L1',lw=1.5)
pl.plot(f2[:,1],f2[:,3],'b:',label='L2',lw=2)
pl.plot(f3[:,1],f3[:,3],'g--',label='L3',lw=2)
pl.plot(f4[:,1],f4[:,3],'m-.',label='L4',lw=2)
pl.ylim([0,15])
pl.xlim([210,70])
#pl.title('rms source comparison')
pl.xlabel('$\\nu_{\\rm obs}\; \\rm{[MHz]}$')
pl.ylabel('$<\delta T_{\\rm b}>^{1/2}\; \\rm{[mK]}$')
pl.minorticks_on()
leg = pl.legend(loc='upper left',prop={'size':11})
leg.draw_frame(False)
pl.savefig('./eps/latest_dTrms_244_rsd_sources.eps')
pl.savefig('./png/latest_dTrms_244_rsd_sources.png')

pl.clf()
pl.plot(f1[:,1],f1[:,7],'r-',lw=1.5,label='L1')
pl.plot(f2[:,1],f2[:,7],'b:',lw=2,label='L2')
pl.plot(f3[:,1],f3[:,7],'g--',lw=2,label='L3')
pl.plot(f4[:,1],f4[:,7],'m-.',lw=2,label='L4')
#pl.plot(f1[:,1],f1[:,7],'r',label='no LMACHs')
#pl.plot(f2[:,1],f2[:,7],'b',label='supp LMACHs')
#pl.plot(f3[:,1],f3[:,7],'g',label='psupp LMACHs')
#pl.plot(f4[:,1],f4[:,7],'m',label='gsupp LMACHs')
pl.ylim([0,7])
pl.xlim([210,70])
#pl.title('rms Source comparison with 5" beam, 0.4 MHz')
pl.xlabel('$\\nu_{\\rm obs}\; \\rm{[MHz]}$')
pl.ylabel('$<\delta T_{\\rm b}>^{1/2} \\rm{[mK]}$')
pl.minorticks_on()
leg = pl.legend(loc='upper left',prop={'size':11})
leg.draw_frame(False)
pl.savefig('./eps/latest_dTrms_244_rsd_b5nu4_sources.eps')
pl.savefig('./png/latest_dTrms_244_rsd_b5nu4_sources.png')
'''
pl.clf()
pl.plot(f1[:,1],f1[:,2],'r-',lw=1.5,label='L1')
pl.plot(f2[:,1],f2[:,2],'b:',lw=2,label='L2')
pl.plot(f3[:,1],f3[:,2],'g--',lw=2,label='L3')
pl.plot(f4[:,1],f4[:,2],'m-.',lw=2,label='L4')
pl.ylim([0,40])
pl.xlim([210,70])
#pl.title('mean dT source comparison')
pl.xlabel('$\\nu_{\\rm obs}\; \\rm{[MHz]}$')
pl.ylabel('$\\overline{\delta T}_{\\rm b}\; \\rm{[mK]}$')
leg = pl.legend(loc='upper left',prop={'size':11})
leg.draw_frame(False)
pl.savefig('./eps/dTmean_244_rsd_sources.eps')
pl.savefig('./png/dTmean_244_rsd_sources.png')

pl.clf()
pl.plot(f5[:,2],f1[:,3],'r-',lw=1.5,label='L1')
pl.plot(f6[:,2],f2[:,3],'b:',lw=2,label='L2')
pl.plot(f7[:,2],f3[:,3],'g--',lw=2,label='L3')
pl.plot(f8[:,2],f4[:,3],'m-.',lw=2,label='L4')
#pl.plot(f5[:,2],f1[:,3],'r',lw=2,label='no LMACHs')
#pl.plot(f6[:,2],f2[:,3],'b',lw=2,label='supp LMACHs')
#pl.plot(f7[:,2],f3[:,3],'g',lw=2,label='psupp LMACHs')
#pl.plot(f8[:,2],f4[:,3],'m',lw=2,label='gsupp LMACHs')
pl.ylim([0,9])
pl.xlim([1.05,-0.05])
#pl.title('rms comparison vs. ionized fraction')
pl.xlabel('$x_{\\rm m}$')
pl.ylabel('$<\delta T_{\\rm b}>^{1/2}\; \\rm{[mK]}$')
pl.minorticks_on()
leg = pl.legend(loc='upper left',prop={'size':11})
leg.draw_frame(False)
pl.savefig('./eps/dTrmsxi_244_rsd_sources.eps')
pl.savefig('./png/dTrmsxi_244_rsd_sources.png')

pl.clf()
pl.plot(f5[:,2],f1[:,7],'r-',lw=1.5,label='L1')
pl.plot(f6[:,2],f2[:,7],'b:',lw=2,label='L2')
pl.plot(f7[:,2],f3[:,7],'g--',lw=2,label='L3')
pl.plot(f8[:,2],f4[:,7],'m-.',lw=2,label='L4')
#pl.plot(f5[:,2],f1[:,7],'r',label='no LMACHs')
#pl.plot(f6[:,2],f2[:,7],'b',label='supp LMACHs')
#pl.plot(f7[:,2],f3[:,7],'g',label='psupp LMACHs')
#pl.plot(f8[:,2],f4[:,7],'m',label='gsupp LMACHs')
pl.ylim([0,5])
pl.xlim([1.05,-0.05])
#pl.title('rms source comparison with 5" beam, 0.4 MHz')
pl.xlabel('$x_{\\rm m}$')
pl.ylabel('$<\delta T_{\\rm b}>^{1/2}\; \\rm{[mK]}$')
pl.minorticks_on()
leg = pl.legend(loc='upper left',prop={'size':11})
leg.draw_frame(False)
pl.savefig('./eps/dTrmsxi_244_rsd_b5nu4_sources.eps')
pl.savefig('./png/dTrmsxi_244_rsd_b5nu4_sources.png')

pl.clf()
fg = gridspec.GridSpec(3,1)
fg.update(hspace=0)
up = pl.subplot(fg[0, :])
up.plot(f1[:,1],f1[:,3],'r-',label='L1',lw=1.5)
up.plot(f2[:,1],f2[:,3],'b:',label='L2',lw=2)
up.plot(f3[:,1],f3[:,3],'g--',label='L3',lw=2)
up.plot(f4[:,1],f4[:,3],'m-.',label='L4',lw=2)
up.set_ylabel('$\\overline{\delta T}_{\\rm b}\; \\rm{[mK]}$')
up.set_ylim([0,39])
up.set_xlim([210,70])
up.minorticks_on()
up_yax = up.axes.get_yaxis() 
up_yax.set_major_locator(MaxNLocator(integer=True))
low = pl.subplot(fg[1:, :])
low.plot(f1[:,1],f1[:,7],'r-',label='L1',lw=1.5)
low.plot(f2[:,1],f2[:,7],'b:',label='L2',lw=2)
low.plot(f3[:,1],f3[:,7],'g--',label='L3',lw=2)
low.plot(f4[:,1],f4[:,7],'m-.',label='L4',lw=2)
low.set_ylim([0,5])
low.set_xlim([210,70])
leg = up.legend(loc='lower right',prop={'size':12})
leg.draw_frame(False)
low.set_ylabel('$<\delta T_{\\rm b}>^{1/2}\; \\rm{[mK]}$')
low.set_xlabel('$\\nu_{\\rm obs}\; \\rm{[MHz]}$')
low.minorticks_on()

pl.setp(up.get_xticklabels(), visible=False)
pl.minorticks_on()
pl.savefig('./eps/dTmeanrms_244_rsd_b5nu4_sources.eps')
pl.savefig('./png/dTmeanrms_244_rsd_b5nu4_sources.png')

pl.clf()
fg = gridspec.GridSpec(1,1)
fg.update(hspace=0)
fig = pl.subplot(fg[0, :])
fig.plot(f1[:,1],f1[:,7],'r-',lw=1.5,label='L1')
fig.plot(f2[:,1],f2[:,7],'b:',lw=2,label='L2')
fig.plot(f3[:,1],f3[:,7],'g--',lw=2,label='L3')
fig.plot(f4[:,1],f4[:,7],'m-.',lw=2,label='L4')
fig.set_ylim([0,5])
fig.set_xlim([210,70])
fig.set_xlabel('$\\nu_{\\rm obs}\; \\rm{[MHz]}$')
fig.set_ylabel('$<\delta T_{\\rm b}>^{1/2} \\rm{[mK]}$')
fig.minorticks_on()
leg = fig.legend(loc='upper left',prop={'size':11})
leg.draw_frame(False)
mpl.rcParams['xtick.labelsize'] = 11
mpl.rcParams['ytick.labelsize'] = 11
a = inset_axes(fig.axes, width="30%", height="30%",loc=4) #width="30%", height="30%",add_axes([7, 4, 1, 1])
a.plot(f1[:,1],f1[:,2],'r-',lw=1.1)
a.plot(f2[:,1],f2[:,2],'b:',lw=1.5)
a.plot(f3[:,1],f3[:,2],'g--',lw=1.5)
a.plot(f4[:,1],f4[:,2],'m-.',lw=1.5)
a.set_ylim([0,39])
a.set_xlim([209,69])
a.get_xaxis().set_visible(False)
pl.savefig('./eps/dTinset_244_rsd_b5nu4_sources.eps')
pl.savefig('./png/dTinset_244_rsd_b5nu4_sources.png')

'''
