#This file illustrates some basic usage for the c2raytools package
#The script reads some data files and prints and plots some statistics

import c2raytools as c2t
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator

#Some path names. Modify these as needed
one_filename = 'ps_raw_244Mpc_0_7.525.dat'
two_filename =	'ps_raw_244Mpc_0_7.059.dat'
three_filename = 'ps_raw_244Mpc_0_6.483.dat'
four_filename = 'ps_rsd_244Mpc_0_7.525.dat'
five_filename =	'ps_rsd_244Mpc_0_7.059.dat'
six_filename = 'ps_rsd_244Mpc_0_6.483.dat'
seven_filename = 'new2_ps_lc_244Mpc_0_7.524.dat'
eight_filename =	'new2_ps_lc_244Mpc_0_7.058.dat'
nine_filename = 'new2_ps_lc_244Mpc_0_6.482.dat'
#four_filename = 'xfrac_244Mpc_f2_gS_250'

#Enable the printing of various messages
#c2t.utils.set_verbose(True)

#We are using the 47/h Mpc simulation box, so set all the proper conversion factors
#c2t.set_sim_constants(boxsize_cMpc = 47.)

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
#f4 = np.loadtxt(four_filename)

pl.figure()
fg = gridspec.GridSpec(3,1)
fg.update(hspace=0) 
up = pl.subplot(fg[0,:])
up.loglog(f1[:,0],f1[:,0]**3*f1[:,1]/(2*np.pi**2),'r',label='raw')
up.loglog(f4[:,0],f4[:,0]**3*f4[:,1]/(2*np.pi**2),'b',label='rsd')
up.loglog(f7[:,0],f7[:,0]**3*f7[:,1]/(2*np.pi**2),'g',label='lc')
up.text(.05,70,'$z=7.52,$ $x_m=0.3$')
up.set_xlim([0.04,5])
up.set_ylim([0,200])
up.set_title('Dimensionless power spectra')
mid = pl.subplot(fg[1,:])
mid.loglog(f2[:,0],f2[:,0]**3*f2[:,1]/(2*np.pi**2),'r',label='raw')
mid.loglog(f5[:,0],f5[:,0]**3*f5[:,1]/(2*np.pi**2),'b',label='rsd')
mid.loglog(f8[:,0],f8[:,0]**3*f8[:,1]/(2*np.pi**2),'g',label='lc')
mid.set_ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
mid.text(.05,70,'$z=7.06,$ $x_m=0.5$')
mid.set_xlim([0.04,5])
mid.set_ylim([0,200])
low = pl.subplot(fg[2,:])
low.loglog(f2[:,0],f2[:,0]**3*f2[:,1]/(2*np.pi**2),'r',label='raw')
low.loglog(f5[:,0],f5[:,0]**3*f5[:,1]/(2*np.pi**2),'b',label='rsd')
low.loglog(f8[:,0],f8[:,0]**3*f8[:,1]/(2*np.pi**2),'g',label='lc')
low.legend(loc='lower left',prop={'size':12})
low.text(.05,70,'$z=6.48,$ $x_m=0.9$')
low.set_xlim([0.04,5])
low.set_ylim([0,200])
pl.xlim([0.04,5])
#pl.ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
pl.xlabel('$k$ [Mpc$^{-1}$]',fontsize=16)
pl.legend(loc='lower right',prop={'size':12})

pl.savefig('ps_244Mpc_0_zall.png')

#Plot volume and mass neutral fractions
'''pl.figure()
pl.loglog(f1[:,0],f1[:,0]**3*f1[:,1]/(2*np.pi**2),'r',label='raw')
pl.loglog(f4[:,0],f4[:,0]**3*f4[:,1]/(2*np.pi**2),'b',label='rsd')
pl.loglog(f7[:,0],f7[:,0]**3*f7[:,1]/(2*np.pi**2),'g',label='lc')
#pl.ylim([0,200])
pl.xlim([0.04,5])
#pl.ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
pl.xlabel('$k$ [Mpc$^{-1}$]',fontsize=16)
pl.legend(loc='lower right',prop={'size':12})
pl.title('Dimensionless power spectra')
pl.savefig('ps_244Mpc_0_zall.png')

pl.clf()
pl.loglog(f2[:,0],f2[:,0]**3*f2[:,1]/(2*np.pi**2),'r',label='raw')
pl.loglog(f5[:,0],f5[:,0]**3*f5[:,1]/(2*np.pi**2),'b',label='rsd')
pl.loglog(f8[:,0],f8[:,0]**3*f8[:,1]/(2*np.pi**2),'g',label='lc')
pl.ylim([0,200])
pl.xlim([0.04,5])
pl.ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
pl.xlabel('$k$ [Mpc$^{-1}$]',fontsize=16)
pl.legend(loc='lower right',prop={'size':12})
pl.title('Dimensionless power spectrum at $x_m = 0.5$')
pl.savefig('ps_244Mpc_0_z7.06.png')

pl.clf()
pl.loglog(f3[:,0],f3[:,0]**3*f3[:,1]/(2*np.pi**2),'r',label='raw')
pl.loglog(f6[:,0],f6[:,0]**3*f6[:,1]/(2*np.pi**2),'b',label='rsd')
pl.loglog(f9[:,0],f9[:,0]**3*f9[:,1]/(2*np.pi**2),'g',label='lc')
pl.ylim([0,200])
pl.xlim([0.04,5])
pl.ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
pl.xlabel('$k$ [Mpc$^{-1}$]',fontsize=16)
pl.legend(loc='lower right',prop={'size':12})
pl.title('Dimensionless power spectrum at $x_m = 0.9$')
pl.savefig('ps_244Mpc_0_z6.48.png')'''

pl.clf()
pl.loglog(f7[:,0],f7[:,0]**3*f7[:,2]/(2*np.pi**2),'r',label='$z=7.52,$ $x_m=0.3$')
pl.loglog(f8[:,0],f8[:,0]**3*f8[:,2]/(2*np.pi**2),'b',label='$z=7.06,$ $x_m=0.5$')
pl.loglog(f9[:,0],f9[:,0]**3*f9[:,2]/(2*np.pi**2),'g',label='$z=6.48,$ $x_m=0.9$')
pl.loglog(f7[:,0],f7[:,0]**3*f7[:,1]/(2*np.pi**2),'r--')#,label='$z=8.515,$ $x_m=0.1$')
pl.loglog(f8[:,0],f8[:,0]**3*f8[:,1]/(2*np.pi**2),'b--')#,label='$z=7.059,$ $x_m=0.1$')
pl.loglog(f9[:,0],f9[:,0]**3*f9[:,1]/(2*np.pi**2),'g--')#,label='$z=6.483,$ $x_m=0.1$')
pl.ylim([0,200])
pl.xlim([0.04,5])
pl.ylabel('$\Delta^2_{21cm}(k)$ [mK$^2$]',fontsize=16)
pl.xlabel('$k$ [Mpc$^{-1}$]',fontsize=16)
pl.legend(loc='upper left',prop={'size':12})
pl.title('Including 5" beam and 0.4 Mhz filter (lightcone only, raw is dashed)')
pl.savefig('lc_ps_244Mpc_0.png')

'''
fg = gridspec.GridSpec(2,1)
fg.update(hspace=0) 
up = pl.subplot(fg[0, :])
#up.plot(np.log10(f1[:,0]),f1[:,1],'r',f2[:,0],f2[:,2]/f2[:,1],'b',f3[:,0],f3[:,2]/f3[:,1],'g',f4[:,0],f4[:,2]/f4[:,1],'m')
up.plot(f1[:,0],f1[:,1],'r',label='$z=8.515, x_m=0.1$')
up.plot(f2[:,0],f2[:,1],'b',label='$z=7.059, x_m=0.5$')
up.plot(f3[:,0],f3[:,1],'g',label='$z=6.483, x_m=0.9$')
up.legend(loc='upper left',prop={'size':12})
#up.plot(np.log10(f4[:,2]),'m',label='gsupp LMACHs')
up.set_ylabel('PDF',fontsize=16)
up.set_ylim([0,2])
up.set_xlim([-23,-10])
up_yax = up.axes.get_yaxis() 
up_yax.set_major_locator(MaxNLocator(integer=True))
#low = pl.subplot2grid((5,1),(1,0), rowspan=4, sharex=up)
low = pl.subplot(fg[1, :])
low.plot(f1[:,0],np.log10(f1[:,1]),'r',label='$z=8.515, x_m=0.1$')
low.plot(f2[:,0],np.log10(f2[:,1]),'b',label='$z=8.515, x_m=0.1$')
low.plot(f3[:,0],np.log10(f3[:,1]),'g',label='$z=8.515, x_m=0.1$')
low.set_ylim([-6,0.5])
low.set_ylabel('$lg(PDF)$',fontsize=16)
low.set_xlabel('$lg(\Gamma)$',fontsize=16)
#low.legend(loc='upper right',prop={'size':12})
#fg.subplots_adjust(hspace=0)
pl.xlim([-23,-10])
pl.setp(up.get_xticklabels(), visible=False)
pl.minorticks_on()
pl.show()
pl.savefig('ps_244Mpc_0.png')'''

