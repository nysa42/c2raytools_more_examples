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
#one_filename = '../1244Mpc_f2_0_250_pyt/results/xid_ps_244Mpc_0_250_7.525.dat'
#two_filename =	'../1244Mpc_f2_0_250_pyt/results/xid_ps_244Mpc_0_250_7.059.dat'
#three_filename = '../1244Mpc_f2_0_250_pyt/results/xid_ps_244Mpc_0_250_6.757.dat'
one_filename = '../1244Mpc_f2_0_250_pyt/results/binsps_244Mpc_0_250_7.525.dat'
two_filename =	'../1244Mpc_f2_0_250_pyt/results/binsps_244Mpc_0_250_7.059.dat'
three_filename = '../1244Mpc_f2_0_250_pyt/results/binsps_244Mpc_0_250_6.757.dat'
four_filename = '../1244Mpc_f2_0_250_pyt/Mao_ps/output/powers/7.570_21cmpowers_monopole_2x.dat'
five_filename =	'../1244Mpc_f2_0_250_pyt/Mao_ps/output/powers/7.059_21cmpowers_monopole_2x.dat'
six_filename = '../1244Mpc_f2_0_250_pyt/Mao_ps/output/powers/6.757_21cmpowers_monopole_2x.dat'

#Read in xfrac files
f1 = np.loadtxt(one_filename,skiprows=2)
f2 = np.loadtxt(two_filename,skiprows=2)
f3 = np.loadtxt(three_filename,skiprows=2)
f4 = np.loadtxt(four_filename,skiprows=2)
f5 = np.loadtxt(five_filename,skiprows=2)
f6 = np.loadtxt(six_filename,skiprows=2)

pl.figure()
fg = gridspec.GridSpec(3,1)
fg.update(hspace=0) 
up = pl.subplot(fg[0,:])
up.loglog(f1[:,0],f1[:,0]**3*f1[:,1]/(2*np.pi**2),'r-',label='$\delta T_{\\rm b}$',lw=0.75)
#up.loglog(f1[:,0],f1[:,0]**3*f1[:,3]/(2*np.pi**2),'r:',label='$x_{\\rm HI}$',lw=1.3)
#up.loglog(f1[:,0],f1[:,0]**3*f1[:,4]/(2*np.pi**2),'r--',label='$\delta_{\\rm \\rho}$',lw=1)
#up.loglog(f1[:,0],f1[:,0]**3*f1[:,5]/(2*np.pi**2),'r-.',label='$\delta_{\\rm \\rho}x_{\\rm HI}$',lw=1)
#up.loglog(f1[:,0],-1*f1[:,0]**3*f1[:,5]/(2*np.pi**2),'k-.')
up.loglog(f4[:,2]*.7,f4[:,3],'r-',label='Mao',lw=0.25)
#up.loglog(f4[:,2]*.7,f4[:,8],'r--',label='$\mu_0$',lw=1)
#up.loglog(f4[:,2]*.7,f4[:,9],'r:',label='$\mu_2$',lw=1.5)
#up.loglog(f4[:,2]*.7,f4[:,10],'r-.',label='$\mu_4$',lw=1)
#up.loglog(f1[:,0],f1[:,0]**3*f1[:,1]/(2*np.pi**2),'r',label='no LMACHs')
#up.loglog(f4[:,0],f4[:,0]**3*f4[:,1]/(2*np.pi**2),'b',label='supp LMACHs')
#up.loglog(f7[:,0],f7[:,0]**3*f7[:,1]/(2*np.pi**2),'g',label='psupp LMACHs')
#up.loglog(f10[:,0],f10[:,0]**3*f10[:,1]/(2*np.pi**2),'m',label='gsupp LMACHs')
up.text(.05,40,'$x_m=0.3$')
up.set_xlim([0.01,15])
up.set_ylim([-5,200])
#up.set_title('Comparison of source models')
leg = up.legend(loc='lower right',prop={'size':10})
leg.draw_frame(False)
mid = pl.subplot(fg[1,:])
mid.loglog(f2[:,0],f2[:,0]**3*f2[:,1]/(2*np.pi**2),'r-',lw=0.75)
#mid.loglog(f2[:,0],f2[:,0]**3*f2[:,3]/(2*np.pi**2),'r:',lw=1)
#mid.loglog(f2[:,0],f2[:,0]**3*f2[:,4]/(2*np.pi**2),'r--',lw=1)
#mid.loglog(f2[:,0],f2[:,0]**3*f2[:,5]/(2*np.pi**2),'r-.',label='$\delta_{\\rm \\rho}x_{\\rm HI}$',lw=1)
#mid.loglog(f2[:,0],-1*f2[:,0]**3*f2[:,5]/(2*np.pi**2),'k-.')
mid.loglog(f5[:,2]*.7,f5[:,3],'r-',lw=0.25)
#mid.loglog(f5[:,2]*.7,f5[:,8],'r--',lw=1)
#mid.loglog(f5[:,2]*.7,f5[:,9],'r--',lw=1.5)
#mid.loglog(f5[:,2]*.7,f5[:,10],'r-.',lw=1)
mid.set_ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
mid.text(.05,80,'$x_m=0.5$')
mid.set_xlim([0.01,15])
mid.set_ylim([0.01,200])
low = pl.subplot(fg[2,:])
low.loglog(f3[:,0],f3[:,0]**3*f3[:,1]/(2*np.pi**2),'r-',lw=0.75)
#low.loglog(f3[:,0],f3[:,0]**3*f3[:,3]/(2*np.pi**2),'r:',lw=1)
#low.loglog(f3[:,0],f3[:,0]**3*f3[:,4]/(2*np.pi**2),'r--',lw=1)
#low.loglog(f3[:,0],f3[:,0]**3*f3[:,5]/(2*np.pi**2),'r-.',label='$\delta_{\\rm \\rho}x_{\\rm HI}$',lw=1)
#low.loglog(f3[:,0],-1*f3[:,0]**3*f3[:,5]/(2*np.pi**2),'k-.')
low.loglog(f6[:,2]*.7,f6[:,3],'r-',lw=0.25)
#low.loglog(f6[:,2]*.7,f6[:,8],'r--',lw=1)
#low.loglog(f6[:,2]*.7,f6[:,9],'r:',lw=1.5)
#low.loglog(f6[:,2]*.7,f6[:,10],'r-.',lw=1)
#low.legend(loc='lower left',prop={'size':12})
low.text(.05,18,'$x_m=0.7$')
low.set_xlim([0.01,15])
low.set_ylim([0.05,80])
#pl.xlim([0.01,5])
#pl.ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
pl.xlabel('$k$ [Mpc$^{-1}$]',fontsize=16)
#pl.legend(loc='lower right',prop={'size':12})

pl.savefig('./png/bins_ps_244Mpc_f2_0_250.png')
