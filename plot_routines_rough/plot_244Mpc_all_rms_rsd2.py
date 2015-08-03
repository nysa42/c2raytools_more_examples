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
one_filename = '../1244Mpc_f2_0_250_pyt/results/dT_rsd_b5nu73_244Mpc_0_250.dat'
two_filename =	'../1244Mpc_f2_8.2S_250_pyt/results/dT_rsd_b5nu73_244Mpc_8.2S_250.dat'
three_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/dT_rsd_b5nu73_244Mpc_8.2pS_250.dat'
four_filename = '../1244Mpc_f2_gS_250_pyt/results/dT_rsd_b5nu73_244Mpc_gS_250.dat'
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
pl.plot(f5[:,2],f1[:,7],'r-',lw=1.5,label='L1')
pl.plot(f6[:,2],f2[:,7],'b:',lw=2,label='L2')
pl.plot(f7[:,2],f3[:,7],'g--',lw=2,label='L3')
pl.plot(f8[:,2],f4[:,7],'m-.',lw=2,label='L4')
#pl.plot(f5[:,2],f1[:,7],'r',label='no LMACHs')
#pl.plot(f6[:,2],f2[:,7],'b',label='supp LMACHs')
#pl.plot(f7[:,2],f3[:,7],'g',label='psupp LMACHs')
#pl.plot(f8[:,2],f4[:,7],'m',label='gsupp LMACHs')
pl.ylim([0,5.5])
pl.xlim([1.05,-0.05])
#pl.title('rms source comparison with 5" beam, 0.4 MHz')
pl.xlabel('$x_{\\rm m}$')
pl.ylabel('$\langle\delta T_{\\rm b}\\rangle^{1/2}\, \\rm{[mK]}$')
pl.minorticks_on()
leg = pl.legend(loc='lower right',prop={'size':11})
leg.draw_frame(False)
pl.savefig('./eps/dTrmsxi_244_rsd_b5nu73_sources.eps')
pl.savefig('./png/dTrmsxi_244_rsd_b5nu73_sources.png')

