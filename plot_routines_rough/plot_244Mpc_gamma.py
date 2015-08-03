#This file illustrates some basic usage for the c2raytools package
#The script reads some data files and prints and plots some statistics


import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl

mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['axes.labelsize'] = 17

#Some path names. Modify these as needed
one_filename = '../1244Mpc_f2_0_250_pyt/results/meanG_244Mpc_f2_0_250.dat'
two_filename =	'../1244Mpc_f2_8.2S_250_pyt/results/meanG_244Mpc_f2_8.2S_250.dat'
three_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/meanG_244Mpc_f2_8.2pS_250.dat'
four_filename = '../1244Mpc_f2_gS_250_pyt/results/meanG_244Mpc_f2_gS_250.dat'

#Read in mean photoionization rate files: z, avg_vol, avg_mass 
f1 = np.loadtxt(one_filename)
f2 = np.loadtxt(two_filename)
f3 = np.loadtxt(three_filename)
f4 = np.loadtxt(four_filename)

Bolt_z2 = 6.      # McGreer et al 2015 (upper limit)
Bolt_x2 = 1.8e-13
Bolt_u2 = 1.8e-13
Bolt_l2 = 9.e-14

#Plot volume and mass neutral fractions
pl.figure()
pl.plot(f1[:,0],np.log10(f1[:,1]),'r-',lw=1.5,label='L1')
pl.plot(f2[:,0],np.log10(f2[:,1]),'b:',lw=2,label='L2')
pl.plot(f3[:,0],np.log10(f3[:,1]),'g--',lw=2,label='L3')
pl.plot(f4[:,0],np.log10(f4[:,1]),'m-.',lw=2,label='L4')
pl.errorbar(Bolt_z2,np.log10(Bolt_x2),0.27,0.,marker='h', color='c',label='Wyithe & Bolton (2011)')
pl.xlim([5.7,14])
#pl.title('Volume-weighted')
pl.xlabel('$z$')
pl.ylabel('$\mathrm{log_{10}}(\\overline{\Gamma})$')
pl.minorticks_on()
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)
pl.savefig('./png/Gamma_mean_244Mpc_250_vol.png')
pl.savefig('./eps/Gamma_mean_244Mpc_250_vol.eps')
