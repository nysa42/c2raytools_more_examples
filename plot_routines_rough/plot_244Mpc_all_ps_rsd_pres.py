#This file illustrates some basic usage for the c2raytools package
#The script reads some data files and prints and plots some statistics

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator

mpl.rcParams['axes.linewidth'] = 1.5

#Some path names. Modify these as needed
one_filename = '../244Mpc_f2_0_250_pyt/results/ps_rsd_244Mpc_0_250_7.525.dat'
two_filename =	'../244Mpc_f2_0_250_pyt/results/ps_rsd_244Mpc_0_250_7.059.dat'
three_filename = '../244Mpc_f2_0_250_pyt/results/ps_rsd_244Mpc_0_250_6.483.dat'
four_filename = '../244Mpc_f2_8.2S_250_pyt/results/ps_rsd_244Mpc_8.2S_250_7.960.dat'
five_filename =	'../244Mpc_f2_8.2S_250_pyt/results/ps_rsd_244Mpc_8.2S_250_7.263.dat'
six_filename = '../244Mpc_f2_8.2S_250_pyt/results/ps_rsd_244Mpc_8.2S_250_6.617.dat'
seven_filename = '../244Mpc_f2_8.2pS_250_pyt/results/ps_rsd_244Mpc_8.2pS_250_9.457.dat'
eight_filename =	'../244Mpc_f2_8.2pS_250_pyt/results/ps_rsd_244Mpc_8.2pS_250_8.636.dat'
nine_filename = '../244Mpc_f2_8.2pS_250_pyt/results/ps_rsd_244Mpc_8.2pS_250_7.859.dat'
ten_filename = '../244Mpc_f2_gS_250_pyt/results/ps_rsd_244Mpc_gS_250_8.340.dat'
eleven_filename =	'../244Mpc_f2_gS_250_pyt/results/ps_rsd_244Mpc_gS_250_7.712.dat'
twelve_filename = '../244Mpc_f2_gS_250_pyt/results/ps_rsd_244Mpc_gS_250_6.981.dat'


#Read in xfrac files
f1 = np.loadtxt(one_filename,skiprows=3)
f2 = np.loadtxt(two_filename,skiprows=3)
f3 = np.loadtxt(three_filename,skiprows=3)
f4 = np.loadtxt(four_filename,skiprows=3)
f5 = np.loadtxt(five_filename,skiprows=3)
f6 = np.loadtxt(six_filename,skiprows=3)
f7 = np.loadtxt(seven_filename,skiprows=3)
f8 = np.loadtxt(eight_filename,skiprows=3)
f9 = np.loadtxt(nine_filename,skiprows=3)
f10 = np.loadtxt(ten_filename,skiprows=3)
f11 = np.loadtxt(eleven_filename,skiprows=3)
f12 = np.loadtxt(twelve_filename,skiprows=3)

pl.figure()
fg = gridspec.GridSpec(3,1)
fg.update(hspace=0) 
up = pl.subplot(fg[0,:])
#up.loglog(f1[:,0],f1[:,0]**3*f1[:,1]/(2*np.pi**2),'r-',label='L1',lw=1.5)
#up.loglog(f4[:,0],f4[:,0]**3*f4[:,1]/(2*np.pi**2),'b:',label='L2',lw=2)
#up.loglog(f7[:,0],f7[:,0]**3*f7[:,1]/(2*np.pi**2),'g--',label='L3',lw=2)
#up.loglog(f10[:,0],f10[:,0]**3*f10[:,1]/(2*np.pi**2),'m-.',label='L4',lw=2)
up.loglog(f1[:,0],f1[:,0]**3*f1[:,1]/(2*np.pi**2),'r',label='no LMACHs')
up.loglog(f4[:,0],f4[:,0]**3*f4[:,1]/(2*np.pi**2),'b',label='supp LMACHs')
up.loglog(f7[:,0],f7[:,0]**3*f7[:,1]/(2*np.pi**2),'g',label='psupp LMACHs')
up.loglog(f10[:,0],f10[:,0]**3*f10[:,1]/(2*np.pi**2),'m',label='gsupp LMACHs')
up.text(.05,200,'$x_m=0.3$')
up.set_xlim([0.04,5])
up.set_ylim([0,500])
#up.set_title('Comparison of source models')
leg = up.legend(loc='lower right',prop={'size':10})
leg.draw_frame(False)
mid = pl.subplot(fg[1,:])
#mid.loglog(f2[:,0],f2[:,0]**3*f2[:,1]/(2*np.pi**2),'r-',lw=1.5)
#mid.loglog(f5[:,0],f5[:,0]**3*f5[:,1]/(2*np.pi**2),'b:',lw=2)
#mid.loglog(f8[:,0],f8[:,0]**3*f8[:,1]/(2*np.pi**2),'g--',lw=2)
#mid.loglog(f11[:,0],f11[:,0]**3*f11[:,1]/(2*np.pi**2),'m-.',lw=2)
mid.loglog(f2[:,0],f2[:,0]**3*f2[:,1]/(2*np.pi**2),'r',label='no LMACHs')
mid.loglog(f5[:,0],f5[:,0]**3*f5[:,1]/(2*np.pi**2),'b',label='supp LMACHs')
mid.loglog(f8[:,0],f8[:,0]**3*f8[:,1]/(2*np.pi**2),'g',label='psupp LMACHs')
mid.loglog(f11[:,0],f11[:,0]**3*f11[:,1]/(2*np.pi**2),'m',label='gsupp LMACHs')
mid.set_ylabel('$\Delta^2_{21\\rm cm}(k)  \\rm{[mK^2]}$',fontsize=16)
mid.text(.05,80,'$x_m=0.5$')
mid.set_xlim([0.04,5])
mid.set_ylim([0.5,270])
low = pl.subplot(fg[2,:])
#low.loglog(f3[:,0],f2[:,0]**3*f3[:,1]/(2*np.pi**2),'r-',lw=1.5)
#low.loglog(f6[:,0],f5[:,0]**3*f6[:,1]/(2*np.pi**2),'b:',lw=2)
#low.loglog(f9[:,0],f9[:,0]**3*f9[:,1]/(2*np.pi**2),'g--',lw=2)
#low.loglog(f12[:,0],f12[:,0]**3*f12[:,1]/(2*np.pi**2),'m-.',lw=2)
low.loglog(f3[:,0],f3[:,0]**3*f3[:,1]/(2*np.pi**2),'r',label='no LMACHs')
low.loglog(f6[:,0],f6[:,0]**3*f6[:,1]/(2*np.pi**2),'b',label='supp LMACHs')
low.loglog(f9[:,0],f9[:,0]**3*f9[:,1]/(2*np.pi**2),'g',label='psupp LMACHs')
low.loglog(f12[:,0],f12[:,0]**3*f12[:,1]/(2*np.pi**2),'m',label='gsupp LMACHs')
#low.legend(loc='lower left',prop={'size':12})
low.text(.05,18,'$x_m=0.9$')
low.set_xlim([0.04,5])
low.set_ylim([1,30])
pl.xlim([0.04,5])
#pl.ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
pl.xlabel('$k  \\rm{[Mpc^{-1}]}$',fontsize=16)
#pl.legend(loc='lower right',prop={'size':12})

pl.savefig('./eps/ps_244Mpc_rsd_source.eps')
pl.savefig('./png/ps_244Mpc_rsd_source.png')
pl.savefig('./pres/ps_244Mpc_rsd_source.png')

pl.clf()
pl.plot(np.log10(f2[:,0]),np.log10(f2[:,0]**3*f3[:,1]/(2*np.pi**2)),'r',label='no LMACHs')
pl.plot(np.log10(f5[:,0]),np.log10(f5[:,0]**3*f6[:,1]/(2*np.pi**2)),'b',label='supp LMACHs')
pl.plot(np.log10(f8[:,0]),np.log10(f8[:,0]**3*f9[:,1]/(2*np.pi**2)),'g',label='psupp LMACHs')
pl.plot(np.log10(f11[:,0]),np.log10(f11[:,0]**3*f12[:,1]/(2*np.pi**2)),'m',label='gsupp LMACHs')
#low.legend(loc='lower left',prop={'size':12})
pl.text(.05,18,'$x_m=0.5$')
pl.xlim([-2,1])
pl.ylim([-0.5,1.5])
#pl.xlim([0.04,5])
pl.ylabel('log10$\Delta^2_{21cm}(k)$\;[mK$^2$]',fontsize=16)
pl.xlabel('log10$k\;\\rm{[Mpc^{-1}]}$',fontsize=16)
pl.savefig('./pres/ps_244Mpc_rsd_log.png')

