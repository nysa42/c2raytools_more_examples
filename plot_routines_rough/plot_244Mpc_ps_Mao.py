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
mpl.rcParams['axes.labelsize'] = 16

#Some path names. Modify these as needed
#one_filename = '../1244Mpc_f2_0_250_pyt/Mao_ps/output/powers/7.525_21cmpowers_monopole_2x.dat'
one_filename = '../1244Mpc_f2_0_250_pyt/Mao_ps/output/powers/7.570_21cmpowers_monopole_2x.dat'
two_filename =	'../1244Mpc_f2_0_250_pyt/Mao_ps/output/powers/7.059_21cmpowers_monopole_2x.dat'
three_filename = '../1244Mpc_f2_0_250_pyt/Mao_ps/output/powers/6.757_21cmpowers_monopole_2x.dat'
four_filename = '../1244Mpc_f2_8.2S_250_pyt/Mao_ps/output/powers/7.960_21cmpowers_monopole_2x.dat'
five_filename =	'../1244Mpc_f2_8.2S_250_pyt/Mao_ps/output/powers/7.305_21cmpowers_monopole_2x.dat'
#six_filename = '../1244Mpc_f2_8.2S_250_pyt/Mao_ps/output/powers/6.617_21cmpowers_monopole_2x.dat'
six_filename = '../1244Mpc_f2_8.2S_250_pyt/Mao_ps/output/powers/6.905_21cmpowers_monopole_2x.dat'
seven_filename = '../1244Mpc_f2_8.2pS_250_pyt/Mao_ps/output/powers/9.457_21cmpowers_monopole_2x.dat'
eight_filename =	'../1244Mpc_f2_8.2pS_250_pyt/Mao_ps/output/powers/8.636_21cmpowers_monopole_2x.dat'
#nine_filename = '../1244Mpc_f2_8.2pS_250_pyt/Mao_ps/output/powers/7.859_21cmpowers_monopole_2x.dat'
nine_filename = '../1244Mpc_f2_8.2pS_250_pyt/Mao_ps/output/powers/8.172_21cmpowers_monopole_2x.dat'
ten_filename = '../1244Mpc_f2_gS_250_pyt/Mao_ps/output/powers/8.397_21cmpowers_monopole_2x.dat'
eleven_filename =	'../1244Mpc_f2_gS_250_pyt/Mao_ps/output/powers/7.760_21cmpowers_monopole_2x.dat'
#twelve_filename = '../1244Mpc_f2_gS_250_pyt/Mao_ps/output/powers/6.981_21cmpowers_monopole_2x.dat'
twelve_filename = '../1244Mpc_f2_gS_250_pyt/Mao_ps/output/powers/7.305_21cmpowers_monopole_2x.dat'


#Read in xfrac files
f1 = np.loadtxt(one_filename,skiprows=2)
f2 = np.loadtxt(two_filename,skiprows=2)
f3 = np.loadtxt(three_filename,skiprows=2)
f4 = np.loadtxt(four_filename,skiprows=2)
f5 = np.loadtxt(five_filename,skiprows=2)
f6 = np.loadtxt(six_filename,skiprows=2)
f7 = np.loadtxt(seven_filename,skiprows=2)
f8 = np.loadtxt(eight_filename,skiprows=2)
f9 = np.loadtxt(nine_filename,skiprows=2)
f10 = np.loadtxt(ten_filename,skiprows=2)
f11 = np.loadtxt(eleven_filename,skiprows=2)
f12 = np.loadtxt(twelve_filename,skiprows=2)

pl.figure()
pl.plot(np.log10(f1[:,2]*0.7+1e-12),np.log10(f1[:,3]+1e-12),'r-',label='L1',lw=1.5)
pl.plot(np.log10(f4[:,2]*0.7+1e-12),np.log10(f4[:,3]+1e-12),'b:',label='L2',lw=2)
pl.plot(np.log10(f7[:,2]*0.7+1e-12),np.log10(f7[:,3]+1e-12),'g--',label='L3',lw=2)
pl.plot(np.log10(f10[:,2]*0.7+1e-12),np.log10(f10[:,3]+1e-12),'m-.',label='L4',lw=2)
pl.xlim([-1.8,0.4])
pl.ylim([-2.1,2.0])
pl.minorticks_on()
pl.xlabel('$\\rm{log_{10}}($$k$$)\, \\rm{[Mpc^{-1}]}$')
pl.ylabel('$\\rm{log_{10}}(\Delta^2_{21\\rm cm})\, \\rm{[mK^2]}$')
pl.text(-1.75,1.75,'$x_{\\rm m}\,=\,0.3$',fontsize=16)
leg = pl.legend(loc='lower right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./eps/ps_244Mpc_Mao_x03.eps')
pl.savefig('./png/ps_244Mpc_Mao_x03.png')

pl.clf()
pl.plot(np.log10(f2[:,2]*0.7+1e-12),np.log10(f2[:,3]+1e-12),'r-',label='L1',lw=1.5)
pl.plot(np.log10(f5[:,2]*0.7+1e-12),np.log10(f5[:,3]+1e-12),'b:',label='L2',lw=2)
pl.plot(np.log10(f8[:,2]*0.7+1e-12),np.log10(f8[:,3]+1e-12),'g--',label='L3',lw=2)
pl.plot(np.log10(f11[:,2]*0.7+1e-12),np.log10(f11[:,3]+1e-12),'m-.',label='L4',lw=2)
pl.xlim([-1.8,0.4])
pl.ylim([-1.05,1.8])
pl.minorticks_on()
pl.xlabel('$\\rm{log_{10}}($$k$$)\, \\rm{[Mpc^{-1}]}$')
pl.ylabel('$\\rm{log_{10}}(\Delta^2_{21\\rm cm})\, \\rm{[mK^2]}$')
pl.text(-1.75,1.625,'$x_{\\rm m}\,=\,0.5$',fontsize=16)
leg = pl.legend(loc='lower right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./eps/ps_244Mpc_Mao_x05.eps')
pl.savefig('./png/ps_244Mpc_Mao_x05.png')

pl.clf()
pl.plot(np.log10(f3[:,2]*0.7+1e-12),np.log10(f3[:,3]+1e-12),'r-',label='L1',lw=1.5)
pl.plot(np.log10(f6[:,2]*0.7+1e-12),np.log10(f6[:,3]+1e-12),'b:',label='L2',lw=2)
pl.plot(np.log10(f9[:,2]*0.7+1e-12),np.log10(f9[:,3]+1e-12),'g--',label='L3',lw=2)
pl.plot(np.log10(f12[:,2]*0.7+1e-12),np.log10(f12[:,3]+1e-12),'m-.',label='L4',lw=2)
pl.xlim([-1.8,0.4])
pl.ylim([-0.5,1.5])
pl.minorticks_on()
pl.xlabel('$\\rm{log_{10}}($$k$$)\, \\rm{[Mpc^{-1}]}$')
pl.ylabel('$\\rm{log_{10}}(\Delta^2_{21\\rm cm})\, \\rm{[mK^2]}$')
pl.text(-1.75,1.38,'$x_{\\rm m}\,=\,0.7$',fontsize=16)
leg = pl.legend(loc='lower right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./eps/ps_244Mpc_Mao_x07.eps')
pl.savefig('./png/ps_244Mpc_Mao_x07.png')
'''
pl.clf()
fg = gridspec.GridSpec(3,1)
fg.update(hspace=0) 
up = pl.subplot(fg[0,:])
up.loglog(f1[:,0],f1[:,0]**3*f1[:,1]/(2*np.pi**2),'r-',label='L1',lw=1.5)
up.loglog(f4[:,0],f4[:,0]**3*f4[:,1]/(2*np.pi**2),'b:',label='L2',lw=2)
up.loglog(f7[:,0],f7[:,0]**3*f7[:,1]/(2*np.pi**2),'g--',label='L3',lw=2)
up.loglog(f10[:,0],f10[:,0]**3*f10[:,1]/(2*np.pi**2),'m-.',label='L4',lw=2)
up.loglog(f1[:,0],f1[:,0]**3*f1[:,1]/(2*np.pi**2),'r',label='no LMACHs')
#up.loglog(f4[:,0],f4[:,0]**3*f4[:,1]/(2*np.pi**2),'b',label='supp LMACHs')
#up.loglog(f7[:,0],f7[:,0]**3*f7[:,1]/(2*np.pi**2),'g',label='psupp LMACHs')
#up.loglog(f10[:,0],f10[:,0]**3*f10[:,1]/(2*np.pi**2),'m',label='gsupp LMACHs')
up.text(.05,150,'$x_{\\rm m}\,=\,0.3$')
up.set_xlim([0.04,5])
up.set_ylim([0,500])
#up.set_title('Comparison of source models')
leg = up.legend(loc='lower right',prop={'size':10})
leg.draw_frame(False)
mid = pl.subplot(fg[1,:])
#mid.loglog(f2[:,0],f2[:,0]**3*f2[:,1]/(2*np.pi**2),'r-',lw=1.5)
mid.loglog(f5[:,0],f5[:,0]**3*f5[:,1]/(2*np.pi**2),'b:',lw=2)
mid.loglog(f8[:,0],f8[:,0]**3*f8[:,1]/(2*np.pi**2),'g--',lw=2)
mid.loglog(f11[:,0],f11[:,0]**3*f11[:,1]/(2*np.pi**2),'m-.',lw=2)
mid.set_ylabel('$\Delta^2_{21\\rm cm}(k)\,  \\rm{[mK^2]}$')
mid.text(.05,120,'$x_{\\rm m}\,=\,0.5$')
mid.set_xlim([0.04,5])
mid.set_ylim([0.5,270])
low = pl.subplot(fg[2,:])
#low.loglog(f3[:,0],f3[:,0]**3*f3[:,1]/(2*np.pi**2),'r-',lw=1.5)
low.loglog(f6[:,0],f6[:,0]**3*f6[:,1]/(2*np.pi**2),'b:',lw=2)
low.loglog(f9[:,0],f9[:,0]**3*f9[:,1]/(2*np.pi**2),'g--',lw=2)
low.loglog(f12[:,0],f12[:,0]**3*f12[:,1]/(2*np.pi**2),'m-.',lw=2)
#low.legend(loc='lower left',prop={'size':12})
low.text(.05,19,'$x_{\\rm m}\,=\,0.9$')
low.set_xlim([0.04,5])
low.set_ylim([1,30])
pl.xlim([0.04,5])
#pl.ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
pl.xlabel('$k\, \\rm{[Mpc^{-1}]}$')
#pl.legend(loc='lower right',prop={'size':12})

pl.savefig('./eps/ps_244Mpc_rsd_source.eps')
pl.savefig('./png/ps_244Mpc_rsd_source.png', bbox_inches='tight')
'''

