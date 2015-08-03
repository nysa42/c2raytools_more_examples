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
one_filename = '../1244Mpc_f2_0_250_pyt/sizes/zahn60_7.525.dat'
two_filename =	'../1244Mpc_f2_0_250_pyt/sizes/zahn60_7.059.dat'
three_filename = '../1244Mpc_f2_0_250_pyt/sizes/zahn60_6.757.dat'
#three_filename = '../1244Mpc_f2_0_250_pyt/sizes/zahn60_6.483.dat'
four_filename = '../1244Mpc_f2_0_500_pyt/sizes/zahn60_7.480.dat'
five_filename =	'../1244Mpc_f2_0_500_pyt/sizes/zahn60_7.059.dat'
six_filename = '../1244Mpc_f2_0_500_pyt/sizes/zahn60_6.757.dat'
#six_filename = '../1244Mpc_f2_0_500_pyt/sizes/zahn60_6.483.dat'
seven_filename = '../1244Mpc_f2_8.2pS_250_pyt/sizes/zahn60_9.457.dat'
eight_filename =	'../1244Mpc_f2_8.2pS_250_pyt/sizes/zahn60_8.636.dat'
nine_filename = '../1244Mpc_f2_8.2pS_250_pyt/sizes/zahn60_8.172.dat'
#nine_filename = '../1244Mpc_f2_8.2pS_250_pyt/sizes/zahn60_7.859.dat'
ten_filename = '../1244Mpc_f2_8.2pS_500_pyt/sizes/zahn60_9.164.dat'
eleven_filename =	'../1244Mpc_f2_8.2pS_500_pyt/sizes/zahn60_8.515.dat'
twelve_filename = '../1244Mpc_f2_8.2pS_500_pyt/sizes/zahn60_8.118.dat'
#twelve_filename = '../1244Mpc_f2_8.2pS_500_pyt/sizes/zahn60_6.981.dat'

#Read in xfrac files
f1 = np.loadtxt(one_filename)
f2 = np.loadtxt(two_filename)
f3 = np.loadtxt(three_filename)
f4 = np.loadtxt(four_filename)
f5 = np.loadtxt(five_filename)
f6 = np.loadtxt(six_filename)
f7 = np.loadtxt(seven_filename)
f8 = np.loadtxt(eight_filename)
f9 = np.loadtxt(nine_filename)
f10 = np.loadtxt(ten_filename)
f11 = np.loadtxt(eleven_filename)
f12 = np.loadtxt(twelve_filename)

pl.figure()
pl.plot(np.log10(f1[:,0]+1e-12),np.log10(f1[:,1]+1e-12),'r-',label='244Mpc_f2_0_250',lw=1.5)
pl.plot(np.log10(f4[:,0]+1e-12),np.log10(f4[:,1]+1e-12),'r:',label='244Mpc_f2_0_500',lw=2)
pl.plot(np.log10(f7[:,0]+1e-12),np.log10(f7[:,1]+1e-12),'g-',label='244Mpc_f2_8.2pS_250',lw=2)
pl.plot(np.log10(f10[:,0]+1e-12),np.log10(f10[:,1]+1e-12),'g:',label='244Mpc_f2_8.2pS_500',lw=2)
pl.text(1.7,0.2,'$x_{\\rm m}\,=\,0.3$',fontsize=16)
pl.xlim([-1.2,2.3])
pl.ylim([-3.8,0.5])
pl.minorticks_on()
pl.xlabel('$\\rm{log_{10}}(R)\; \\rm{[Mpc]}$')
pl.ylabel('$\\rm{log_{10}}(R\; \\rm{dP/d}R)$')
leg = pl.legend(loc='upper left',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/zahn_res_244Mpc_res_x30.png')
pl.savefig('./eps/zahn_res_244Mpc_res_x30.eps')

pl.clf()
pl.plot(np.log10(f2[:,0]+1e-12),np.log10(f2[:,1]+1e-12),'r-',label='244Mpc_f2_0_250',lw=1.5)
pl.plot(np.log10(f5[:,0]+1e-12),np.log10(f5[:,1]+1e-12),'r:',label='244Mpc_f2_0_500',lw=2)
pl.plot(np.log10(f8[:,0]+1e-12),np.log10(f8[:,1]+1e-12),'g-',label='244Mpc_f2_8.2pS_250',lw=2)
pl.plot(np.log10(f11[:,0]+1e-12),np.log10(f11[:,1]+1e-12),'g:',label='244Mpc_f2_8.2pS_500',lw=2)
pl.text(1.7,0.2,'$x_{\\rm m}\,=\,0.5$',fontsize=16)
pl.xlim([-1.2,2.3])
pl.ylim([-3.8,0.5])
pl.minorticks_on()
pl.xlabel('$\\rm{log_{10}}(R)\; \\rm{[Mpc]}$')
pl.ylabel('$\\rm{log_{10}}(R\; \\rm{dP/d}R)$')
leg = pl.legend(loc='upper left',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/zahn_244Mpc_res_x50.png')
pl.savefig('./eps/zahn_244Mpc_res_x50.eps')

'''pl.clf()
pl.plot(np.log10(f3[:,0]+1e-12),np.log10(f3[:,2]+1e-12),'r-',label='244Mpc_f2_0_250',lw=1.5)
pl.plot(np.log10(f6[:,0]+1e-12),np.log10(f6[:,2]+1e-12),'r:',label='244Mpc_f2_0_500',lw=2)
pl.plot(np.log10(f9[:,0]+1e-12),np.log10(f9[:,2]+1e-12),'g-',label='244Mpc_f2_8.2pS_250',lw=2)
#pl.plot(np.log10(f12[:,0]+1e-12),np.log10(f12[:,2]+1e-12),'g:',label='244Mpc_f2_8.2pS_500',lw=2)
pl.text(1.7,0.2,'$x_{\\rm m}\,=\,0.9$',fontsize=16)
pl.xlim([-1.2,2.3])
pl.ylim([-3.8,0.5])
#pl.title('Mass-weighted')
pl.minorticks_on()
pl.xlabel('$\\rm{log_{10}}(R_{\rm neut})\; \\rm{[Mpc]}$')
pl.ylabel('$\\rm{log_{10}}(R{\rm neut}\; \\rm{dP/d}R)$')
leg = pl.legend(loc='upper left',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/zahn_244Mpc_res_n90.png')
pl.savefig('./eps/zahn_244Mpc_res_n90.eps')'''

pl.clf()
pl.plot(np.log10(f3[:,0]+1e-12),np.log10(f3[:,1]+1e-12),'r-',label='244Mpc_f2_0_250',lw=1.5)
pl.plot(np.log10(f6[:,0]+1e-12),np.log10(f6[:,1]+1e-12),'r:',label='244Mpc_f2_0_500',lw=2)
pl.plot(np.log10(f9[:,0]+1e-12),np.log10(f9[:,1]+1e-12),'g-',label='244Mpc_f2_8.2pS_250',lw=2)
pl.plot(np.log10(f12[:,0]+1e-12),np.log10(f12[:,1]+1e-12),'g:',label='244Mpc_f2_8.2pS_500',lw=2)
pl.text(1.7,0.2,'$x_{\\rm m}\,=\,0.7$',fontsize=16)
pl.xlim([-1.2,2.3])
pl.ylim([-3.8,0.5])
#pl.title('Mass-weighted')
pl.minorticks_on()
pl.xlabel('$\\rm{log_{10}}(R)\; \\rm{[Mpc]}$')
pl.ylabel('$\\rm{log_{10}}(R\; \\rm{dP/d}R)$')
leg = pl.legend(loc='upper left',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/zahn_244Mpc_res_x70.png')
pl.savefig('./eps/zahn_244Mpc_res_x70.eps')
