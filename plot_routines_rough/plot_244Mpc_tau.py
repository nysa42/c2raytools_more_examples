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
one_filename = '../1244Mpc_f2_0_250_pyt/results/tau_244Mpc_f2_0_250.dat'
two_filename =	'../1244Mpc_f2_8.2S_250_pyt/results/tau_244Mpc_f2_8.2S_250.dat'
three_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/tau_244Mpc_f2_8.2pS_250.dat'
four_filename = '../1244Mpc_f2_gS_250_pyt/results/tau_244Mpc_f2_gS_250.dat'

#Read in xfrac files
f1 = np.loadtxt(one_filename)
f2 = np.loadtxt(two_filename)
f3 = np.loadtxt(three_filename)
f4 = np.loadtxt(four_filename)

# Planck value and uncertainty
z_p = np.linspace(6,22)
tau_p = 0.066*np.ones(len(z_p))
upper_tau = (0.066+0.013)#*np.ones(len(z_p))
lower_tau = (0.066-0.013)#*np.ones(len(z_p))

#Plot volume and mass neutral fractions
pl.figure()
pl.plot(z_p,tau_p,'k:')
pl.axhspan(lower_tau, upper_tau, facecolor='0.5', alpha=0.1, edgecolor='none')
pl.plot(f1[:,0],f1[:,1],'r-',lw=1.5,label='L1')
pl.plot(f2[:,0],f2[:,1],'b:',lw=2,label='L2')
pl.plot(f3[:,0],f3[:,1],'g--',lw=2,label='L3')
pl.plot(f4[:,0],f4[:,1],'m-.',lw=2,label='L4')
pl.xlim([5.7,16.2])
pl.ylim([0,0.09])
pl.minorticks_on()
#pl.title('Mass-weighted')
pl.xlabel('$z$')
pl.ylabel('$\\tau_{\\rm{es}}$')
leg = pl.legend(loc='lower right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/tau_244Mpc_250.png')
pl.savefig('./eps/tau_244Mpc_250.eps')


