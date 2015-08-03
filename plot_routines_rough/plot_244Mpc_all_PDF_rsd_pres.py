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
#one_filename = '../244Mpc_f2_0_250_pyt/results/dT_PDF_rsd_244Mpc_0_250_7.525.dat'
#two_filename =	'../244Mpc_f2_0_250_pyt/results/dT_PDF_rsd_244Mpc_0_250_7.059.dat'
#three_filename = '../244Mpc_f2_0_250_pyt/results/dT_PDF_rsd_244Mpc_0_250_6.483.dat'
#four_filename = '../244Mpc_f2_8.2S_250_pyt/results/dT_PDF_rsd_244Mpc_8.2S_250_7.960.dat'
#five_filename =	'../244Mpc_f2_8.2S_250_pyt/results/dT_PDF_rsd_244Mpc_8.2S_250_7.263.dat'
#six_filename = '../244Mpc_f2_8.2S_250_pyt/results/dT_PDF_rsd_244Mpc_8.2S_250_6.617.dat'
#seven_filename = '../244Mpc_f2_8.2pS_250_pyt/results/dT_PDF_rsd_244Mpc_8.2pS_250_9.457.dat'
#eight_filename =	'../244Mpc_f2_8.2pS_250_pyt/results/dT_PDF_rsd_244Mpc_8.2pS_250_8.636.dat'
#nine_filename = '../244Mpc_f2_8.2pS_250_pyt/results/dT_PDF_rsd_244Mpc_8.2pS_250_7.859.dat'
#ten_filename = '../244Mpc_f2_gS_250_pyt/results/dT_PDF_rsd_244Mpc_gS_250_8.340.dat'
#eleven_filename =	'../244Mpc_f2_gS_250_pyt/results/dT_PDF_rsd_244Mpc_gS_250_7.712.dat'
#twelve_filename = '../244Mpc_f2_gS_250_pyt/results/dT_PDF_rsd_244Mpc_gS_250_6.981.dat'
one_filename = '../244Mpc_f2_0_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_0_250_7.525.dat'
two_filename =	'../244Mpc_f2_0_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_0_250_7.059.dat'
three_filename = '../244Mpc_f2_0_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_0_250_6.483.dat'
four_filename = '../244Mpc_f2_8.2S_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_8.2S_250_7.960.dat'
five_filename =	'../244Mpc_f2_8.2S_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_8.2S_250_7.263.dat'
six_filename = '../244Mpc_f2_8.2S_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_8.2S_250_6.617.dat'
seven_filename = '../244Mpc_f2_8.2pS_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_8.2pS_250_9.457.dat'
eight_filename =	'../244Mpc_f2_8.2pS_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_8.2pS_250_8.636.dat'
nine_filename = '../244Mpc_f2_8.2pS_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_8.2pS_250_7.859.dat'
ten_filename = '../244Mpc_f2_gS_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_gS_250_8.340.dat'
eleven_filename =	'../244Mpc_f2_gS_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_gS_250_7.712.dat'
twelve_filename = '../244Mpc_f2_gS_250_pyt/results/dT_PDF_rsd_b5nu4_244Mpc_gS_250_6.981.dat'

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
#pl.plot(f1[:,0]-f1[:,2],np.log10(f1[:,1]),'r-',label='L1',lw=1.5)
#pl.plot(f4[:,0]-f4[:,2],np.log10(f4[:,1]),'b:',label='L2',lw=2)
#pl.plot(f7[:,0]-f7[:,2],np.log10(f7[:,1]),'g--',label='L3',lw=2)
#pl.plot(f10[:,0]-f10[:,2],np.log10(f10[:,1]),'m-.',label='L4',lw=2)
pl.plot(f1[:,0]-f1[:,2],np.log10(f1[:,1]),'r',label='no LMACHs')
pl.plot(f4[:,0]-f4[:,2],np.log10(f4[:,1]),'b',label='supp LMACHs')
pl.plot(f7[:,0]-f7[:,2],np.log10(f7[:,1]),'g',label='psupp LMACHs')
pl.plot(f10[:,0]-f10[:,2],np.log10(f10[:,1]),'m',label='gsupp LMACHs')
pl.text(17,-1.3,'$x_m=0.3$',fontsize=16)
pl.xlim([-18,15])
pl.ylim([-5,0])
#pl.title('Mass-weighted')
pl.xlabel('$(\delta T_b-\\bar{\delta T_b}) \\rm{[mK]}$',fontsize=16)
pl.ylabel('$\\rm{log_{10}(PDF)}$',fontsize=16)
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./pres/dT_PDF_rsd_244Mpc_250_x30.png')
#pl.savefig('dT_PDF_rsd_244Mpc_250_x30.eps')

pl.clf()
#pl.plot(f2[:,0]-f2[:,2],np.log10(f2[:,1]+1e-14),'r-',label='L1',lw=1.5)
#pl.plot(f5[:,0]-f5[:,2],np.log10(f5[:,1]+1e-14),'b:',label='L2',lw=2)
#pl.plot(f8[:,0]-f8[:,2],np.log10(f8[:,1]+1e-14),'g--',label='L3',lw=2)
#pl.plot(f11[:,0]-f11[:,2],np.log10(f11[:,1]+1e-14),'m-.',label='L4',lw=2)
pl.plot(f2[:,0]-f2[:,2],np.log10(f2[:,1]+1e-14),'r',label='no LMACHs')
pl.plot(f5[:,0]-f5[:,2],np.log10(f5[:,1]+1e-14),'b',label='supp LMACHs')
pl.plot(f8[:,0]-f8[:,2],np.log10(f8[:,1]+1e-14),'g',label='psupp LMACHs')
pl.plot(f11[:,0]-f11[:,2],np.log10(f11[:,1]+1e-14),'m',label='gsupp LMACHs')
pl.text(17,-1.3,'$x_m=0.5$',fontsize=16)
pl.xlim([-18,15])
pl.ylim([-5,0])
#pl.title('Mass-weighted')
pl.xlabel('$(\delta T_b-\\bar{\delta T_b}) \\rm{[mK]}$',fontsize=16)
pl.ylabel('$\\rm{log_{10}(PDF)}$',fontsize=16)
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./pres/dT_PDF_rsd_244Mpc_250_x50.png')
#pl.savefig('dT_PDF_rsd_244Mpc_250_x50.eps')

pl.clf()
#pl.plot(f3[:,0]-f3[:,2],np.log10(f3[:,1]+1e-14),'r-',label='L1',lw=1.5)
#pl.plot(f6[:,0]-f6[:,2],np.log10(f6[:,1]+1e-14),'b:',label='L2',lw=2)
#pl.plot(f9[:,0]-f9[:,2],np.log10(f9[:,1]+1e-14),'g--',label='L3',lw=2)
#pl.plot(f12[:,0]-f12[:,2],np.log10(f12[:,1]+1e-14),'m-.',label='L4',lw=2)
pl.plot(f3[:,0]-f3[:,2],np.log10(f3[:,1]+1e-14),'r',label='no LMACHs')
pl.plot(f6[:,0]-f6[:,2],np.log10(f6[:,1]+1e-14),'b',label='supp LMACHs')
pl.plot(f9[:,0]-f9[:,2],np.log10(f9[:,1]+1e-14),'g',label='psupp LMACHs')
pl.plot(f12[:,0]-f12[:,2],np.log10(f12[:,1]+1e-14),'m',label='gsupp LMACHs')
pl.text(17,-1.3,'$x_m=0.9$',fontsize=16)
pl.xlim([-18,15])
pl.ylim([-5,0])
#pl.title('Mass-weighted')
pl.xlabel('$(\delta T_b-\\bar{\delta T_b}) \\rm{[mK]}$',fontsize=16)
pl.ylabel('$\\rm{log_{10}(PDF)}$',fontsize=16)
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./pres/dT_PDF_rsd_244Mpc_250_x90.png')
#pl.savefig('dT_PDF_rsd_244Mpc_250_x90.eps')
