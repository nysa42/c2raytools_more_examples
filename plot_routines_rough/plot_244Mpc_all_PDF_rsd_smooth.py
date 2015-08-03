#This file illustrates some basic usage for the c2raytools package
#The script reads some data files and prints and plots some statistics

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator
from scipy.optimize import curve_fit

def gaus(x,a,x0,var):
    return a*np.exp(-(x-x0)**2/(2*var))

mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['axes.labelsize'] = 17

#Some path names. Modify these as needed
one_filename = '../1244Mpc_f2_0_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_0_250_7.525.dat'
two_filename =	'../1244Mpc_f2_0_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_0_250_7.059.dat'
three_filename = '../1244Mpc_f2_0_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_0_250_6.757.dat'
four_filename = '../1244Mpc_f2_8.2S_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_8.2S_250_7.960.dat'
five_filename =	'../1244Mpc_f2_8.2S_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_8.2S_250_7.263.dat'
six_filename = '../1244Mpc_f2_8.2S_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_8.2S_250_6.905.dat'
seven_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_8.2pS_250_9.457.dat'
eight_filename =	'../1244Mpc_f2_8.2pS_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_8.2pS_250_8.636.dat'
nine_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_8.2pS_250_8.172.dat'
ten_filename = '../1244Mpc_f2_gS_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_gS_250_8.340.dat'
eleven_filename =	'../1244Mpc_f2_gS_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_gS_250_7.712.dat'
twelve_filename = '../1244Mpc_f2_gS_250_pyt/results/dT_PDF_rsd_b3nu44_244Mpc_gS_250_7.305.dat'
out_file = 'PDF_fits_244Mpc_rsd_b3nu44.txt'

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
out = open(out_file, 'w')

pl.figure()
pl.plot(f1[:,0]-f1[:,2],np.log10(f1[:,1]),'r-',label='L1',lw=1.5)
#pl.plot(xi1,np.log10(gaus(xi1,*popt1)),'r-',lw=0.5)
pl.plot(f4[:,0]-f4[:,2],np.log10(f4[:,1]),'b:',label='L2',lw=2)
pl.plot(f7[:,0]-f7[:,2],np.log10(f7[:,1]),'g--',label='L3',lw=2)
pl.plot(f10[:,0]-f10[:,2],np.log10(f10[:,1]),'m-.',label='L4',lw=2)
pl.text(-19,-0.3,'$x_{\\rm m}=\,0.3$',fontsize=16) #-19,-0.3
pl.xlim([-19.5,13])
pl.ylim([-5,0])
pl.minorticks_on()
pl.xlabel('$(\delta T_{\\rm b} - \\overline{\delta T}_{\\rm b})\, \\rm{[mK]}$')
pl.ylabel('$\\rm{log_{10}(PDF)}$')
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/dT_PDF_rsd_b3nu44_244Mpc_250_x30.png')
pl.savefig('./eps/dT_PDF_rsd_b3nu44_244Mpc_250_x30.eps')

'''pl.clf()
pl.plot(f1[:,0]-f1[:,2],np.log10(f1[:,1]),'r-',label='L1',lw=1)
pl.plot(f4[:,0]-f4[:,2],np.log10(f4[:,1]),'b-',label='L2',lw=1)
pl.plot(f7[:,0]-f7[:,2],np.log10(f7[:,1]),'g-',label='L3',lw=1)
pl.plot(f10[:,0]-f10[:,2],np.log10(f10[:,1]),'m-',label='L4',lw=1)
pl.plot(f1[:,0]-f1[:,2],np.log10(gaus(f1[:,0]-f1[:,2],1.,f1[:,2][0],f1[:,3][0])),'r:',lw=0.75)
pl.plot(f4[:,0]-f4[:,2],np.log10(gaus(f4[:,0]-f4[:,2],1.,f4[:,2][0],f4[:,3][0])),'b:',lw=0.75)
pl.plot(f7[:,0]-f7[:,2],np.log10(gaus(f7[:,0]-f7[:,2],1.,f7[:,2][0],f7[:,3][0])),'g:',lw=0.75)
pl.plot(f10[:,0]-f10[:,2],np.log10(gaus(f10[:,0]-f10[:,2],1.,f10[:,2][0],f10[:,3][0])),'m:',lw=0.75)
pl.text(-19,-0.3,'$x_{\\rm m}=\,0.3$',fontsize=16)
pl.xlim([-20,13])
pl.ylim([-5,0])
pl.minorticks_on()
pl.xlabel('$(\delta T_{\\rm b} - \\overline{\delta T}_{\\rm b})\, \\rm{[mK]}$')
pl.ylabel('$\\rm{log_{10}(PDF)}$')
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/dT_gPDF_rsd_b3nu44_244Mpc_250_x30.png')
pl.savefig('./eps/dT_gPDF_rsd_b3nu44_244Mpc_250_x30.eps')'''


pl.clf()
pl.plot(f2[:,0]-f2[:,2],np.log10(f2[:,1]+1e-14),'r-',label='L1',lw=1.5)
pl.plot(f5[:,0]-f5[:,2],np.log10(f5[:,1]+1e-14),'b:',label='L2',lw=2)
pl.plot(f8[:,0]-f8[:,2],np.log10(f8[:,1]+1e-14),'g--',label='L3',lw=2)
pl.plot(f11[:,0]-f11[:,2],np.log10(f11[:,1]+1e-14),'m-.',label='L4',lw=2)
pl.text(-14,-0.3,'$x_{\\rm m}=\,0.5$',fontsize=16) #-14,-0.3
pl.xlim([-14.5,13])
pl.ylim([-5,0])
pl.minorticks_on()
pl.xlabel('$(\delta T_{\\rm b} - \\overline{\delta T}_{\\rm b})\, \\rm{[mK]}$')
pl.ylabel('$\\rm{log_{10}(PDF)}$')
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/dT_PDF_rsd_b3nu44_244Mpc_250_x50.png')
pl.savefig('./eps/dT_PDF_rsd_b3nu44_244Mpc_250_x50.eps')

'''pl.clf()
pl.plot(f2[:,0]-f2[:,2],np.log10(f2[:,1]+1e-14),'r-',label='L1',lw=1)
pl.plot(f5[:,0]-f5[:,2],np.log10(f5[:,1]+1e-14),'b-',label='L2',lw=1)
pl.plot(f8[:,0]-f8[:,2],np.log10(f8[:,1]+1e-14),'g-',label='L3',lw=1)
pl.plot(f11[:,0]-f11[:,2],np.log10(f11[:,1]+1e-14),'m-',label='L4',lw=1)
pl.plot(xi1,np.log10(gaus(xi1,*popt1)),'r:',lw=0.75)
pl.plot(xi2,np.log10(gaus(xi2,*popt2)),'b:',lw=0.75)
pl.plot(xi3,np.log10(gaus(xi3,*popt3)),'g:',lw=0.75)
pl.plot(xi4,np.log10(gaus(xi4,*popt4)),'m:',lw=0.75)
pl.text(-14,-0.3,'$x_{\\rm m}=\,0.5$',fontsize=16)
pl.xlim([-15,13])
pl.ylim([-5,0])
pl.minorticks_on()
pl.xlabel('$(\delta T_{\\rm b} - \\overline{\delta T}_{\\rm b})\, \\rm{[mK]}$')
pl.ylabel('$\\rm{log_{10}(PDF)}$')
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/dT_gPDF_rsd_b3nu44_244Mpc_250_x50.png')
pl.savefig('./eps/dT_gPDF_rsd_b3nu44_244Mpc_250_x50.eps')'''


pl.clf()
pl.plot(f3[:,0]-f3[:,2],np.log10(f3[:,1]+1e-14),'r-',label='L1',lw=1.5)
pl.plot(f6[:,0]-f6[:,2],np.log10(f6[:,1]+1e-14),'b:',label='L2',lw=2)
pl.plot(f9[:,0]-f9[:,2],np.log10(f9[:,1]+1e-14),'g--',label='L3',lw=2)
pl.plot(f12[:,0]-f12[:,2],np.log10(f12[:,1]+1e-14),'m-.',label='L4',lw=2)
pl.text(-12,-0.3,'$x_{\\rm m}=\,0.7$',fontsize=16)
pl.xlim([-12.5,14])
pl.ylim([-5,0])
pl.minorticks_on()
#pl.title('Mass-weighted')
pl.xlabel('$(\delta T_{\\rm b} - \\overline{\delta T}_{\\rm b})\, \\rm{[mK]}$',fontsize=16)
pl.ylabel('$\\rm{log_{10}(PDF)}$',fontsize=16)
leg = pl.legend(loc='upper right',prop={'size':12})
leg.draw_frame(False)

pl.savefig('./png/dT_PDF_rsd_b3nu44_244Mpc_250_x70.png')
pl.savefig('./eps/dT_PDF_rsd_b3nu44_244Mpc_250_x70.eps')

out.close()

'''
xi1 = f1[:,0]-f1[:,2]
pi1 = f1[:,1]
var1 = np.sum(xi1**2*pi1**2)
popt1,pcov1 = curve_fit(gaus,xi1,pi1,p0=[1,0,var1])
print '244Mpc_f2_0_250 at 30% a, mu, var = ',popt1
out.write('244Mpc_f2_0_250 at 0.30: a, mu, var = %.3f %.3f %.3f\n' % (popt1[0],popt1[1],popt1[2]))
xi2 = f4[:,0]-f4[:,2]
pi2 = f4[:,1]
var2 = np.sum(xi2**2*pi2**2)
popt2,pcov2 = curve_fit(gaus,xi2,pi2,p0=[1,0,var2])
print '244Mpc_f2_8.2S_250 at 30% a, mu, var = ',popt2
out.write('244Mpc_f2_8.2S_250 at 0.30: a, mu, var = %.3f %.3f %.3f\n' % (popt2[0],popt2[1],popt2[2]))
xi3 = f7[:,0]-f7[:,2]
pi3 = f7[:,1]
var3 = np.sum(xi3**2*pi3**2)
popt3,pcov3 = curve_fit(gaus,xi3,pi3,p0=[1,0,var3])
print '244Mpc_f2_8.2pS_250 at 30% a, mu, var = ',popt3
out.write('244Mpc_f2_8.2pS_250 at 0.30: a, mu, var = %.3f %.3f %.3f\n' % (popt3[0],popt3[1],popt3[2]))
xi4 = f10[:,0]-f10[:,2]
pi4 = f10[:,1]
var4 = np.sum(xi4**2*pi4**2)
popt4,pcov4 = curve_fit(gaus,xi4,pi4,p0=[1,0,var4])
print '244Mpc_f2_gS_250 at 30% a, mu, var = ',popt4
out.write('244Mpc_f2_gS_250 at 0.30: a, mu, var = %.3f %.3f %.3f\n' % (popt4[0],popt4[1],popt4[2]))

xi1 = f2[:,0]-f2[:,2]
pi1 = f2[:,1]
var1 = np.sum(xi1**2*pi1**2)
popt1,pcov1 = curve_fit(gaus,xi1,pi1,p0=[1,0,var1])
print '244Mpc_f2_0_250 at 50% a, mu, var = ',popt1
out.write('244Mpc_f2_0_250 at 0.50: a, mu, var = %.3f %.3f %.3f\n' % (popt1[0],popt1[1],popt1[2]))
xi2 = f5[:,0]-f5[:,2]
pi2 = f5[:,1]
var2 = np.sum(xi2**2*pi2**2)
popt2,pcov2 = curve_fit(gaus,xi2,pi2,p0=[1,0,var2])
print '244Mpc_f2_8.2S_250 at 50% a, mu, var = ',popt2
out.write('244Mpc_f2_8.2S_250 at 0.50: a, mu, var = %.3f %.3f %.3f\n' % (popt2[0],popt2[1],popt2[2]))
xi3 = f8[:,0]-f8[:,2]
pi3 = f8[:,1]
var3 = np.sum(xi3**2*pi3**2)
popt3,pcov3 = curve_fit(gaus,xi3,pi3,p0=[1,0,var3])
print '244Mpc_f2_8.2pS_250 at 50% a, mu, var = ',popt3
out.write('244Mpc_f2_8.2pS_250 at 0.50: a, mu, var = %.3f %.3f %.3f\n' % (popt3[0],popt3[1],popt3[2]))
xi4 = f11[:,0]-f11[:,2]
pi4 = f11[:,1]
var4 = np.sum(xi4**2*pi4**2)
popt4,pcov4 = curve_fit(gaus,xi4,pi4,p0=[1,0,var4])
print '244Mpc_f2_gS_250 at 50% a, mu, var = ',popt4
out.write('244Mpc_f2_gS_250 at 0.50: a, mu, var = %.3f %.3f %.3f\n' % (popt4[0],popt4[1],popt4[2]))
'''
'''xi1 = f3[:,0]-f3[:,2]
pi1 = f3[:,1]
var1 = np.sum(xi1**2*pi1**2)
popt1,pcov1 = curve_fit(gaus,xi1,pi1,p0=[1,0,var1])
print '244Mpc_f2_0_250 at 90% a, mu, var = ',popt1
out.write('244Mpc_f2_0_250 at 0.90: a, mu, var = %.3f %.3f %.3f\n' % (popt1[0],popt1[1],popt1[2]))
xi1 = f6[:,0]-f6[:,2]
pi1 = f6[:,1]
var1 = np.sum(xi1**2*pi1**2)
popt1,pcov1 = curve_fit(gaus,xi1,pi1,p0=[1,0,var1])
print '244Mpc_f2_8.2S_250 at 90% a, mu, var = ',popt1
out.write('244Mpc_f2_8.2S_250 at 0.90: a, mu, var = %.3f %.3f %.3f\n' % (popt1[0],popt1[1],popt1[2]))
xi1 = f9[:,0]-f9[:,2]
pi1 = f9[:,1]
var1 = np.sum(xi1**2*pi1**2)
popt1,pcov1 = curve_fit(gaus,xi1,pi1,p0=[1,0,var1])
print '244Mpc_f2_8.2pS_250 at 90% a, mu, var = ',popt1
out.write('244Mpc_f2_8.2pS_250 at 0.90: a, mu, var = %.3f %.3f %.3f\n' % (popt1[0],popt1[1],popt1[2]))
xi1 = f12[:,0]-f12[:,2]
pi1 = f12[:,1]
var1 = np.sum(xi1**2*pi1**2)
popt1,pcov1 = curve_fit(gaus,xi1,pi1,p0=[1,0,var1])
print '244Mpc_f2_gS_250 at 90% a, mu, var = ',popt1
out.write('244Mpc_f2_gS_250 at 0.90: a, mu, var = %.3f %.3f %.3f\n' % (popt1[0],popt1[1],popt1[2]))'''
