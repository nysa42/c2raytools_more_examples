#This file illustrates some basic usage for the c2raytools package
#The script reads some data files and prints and plots some statistics

import c2raytools as c2t
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator

mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['axes.labelsize'] = 17

#Some path names. Modify these as needed
one_filename = '../1244Mpc_f2_0_250_pyt/results/flux_244Mpc_f2_0_250.dat'
two_filename =	'../1244Mpc_f2_8.2S_250_pyt/results/flux_244Mpc_f2_8.2S_250.dat'
three_filename = '../1244Mpc_f2_8.2pS_250_pyt/results/flux_244Mpc_f2_8.2pS_250.dat'
four_filename =	'../1244Mpc_f2_gS_250_pyt/results/flux_244Mpc_f2_gS_250.dat'

#We are using the 24/h Mpc simulation box, so set all the proper conversion factors
c2t.set_sim_constants(boxsize_cMpc = 244.)

#Read in flux files with zred_now,NumSrc00,NumSrc01,TotSrcFlux0,TotSrcFlux,LargeSrcFlux0,SmallSrcFlux0
# z0, NumSrc1, NumSrc_used2, UnsuppFlux3, UsedFlux4
f1 = np.loadtxt(one_filename)
f2 = np.loadtxt(two_filename)
f3 = np.loadtxt(three_filename)
f4 = np.loadtxt(four_filename)

#Record point of z_ov and create vertical line
zov = [6.231, 6.354, 7.570, 6.757]
print zov[3], f4[:,0]
print np.where(f2[:,0] == zov[1])[0]
y_pos0 = np.where(f1[:,0] == zov[0])[0]
y_pos1 = np.where(f2[:,0] == zov[1])[0]
y_pos2 = np.where(f3[:,0] == zov[2])[0]
y_pos3 = np.where(f4[:,0] == zov[3])[0]

#Need total gas atoms at each z
n_bar = c2t.const.rho_crit_0*c2t.const.OmegaB/(c2t.const.m_p*c2t.const.mean_molecular)*(c2t.conv.LB*c2t.const.Mpc)**3
#print c2t.conv.M_box*c2t.const.OmegaB*.76,n_bar,c2t.const.mean_molecular
n1_bg_z = n_bar#/(1+f1[:,0])**3
n2_bg_z = n_bar#/(1+f2[:,0])**3
n3_bg_z = n_bar#/(1+f3[:,0])**3
n4_bg_z = n_bar#/(1+f4[:,0])**3
print n_bar
#print c2t.const.rho_crit_0*c2t.const.OmegaB/(c2t.const.m_p*c2t.const.mean_molecular)*(425/.7*c2t.const.Mpc)**3

cum_f1 = np.copy(f1[:,4])
for i in np.arange(1,len(cum_f1)):
    cum_f1[i] = cum_f1[i] + cum_f1[i-1]
cum_f2 = np.copy(f2[:,4])
for i in np.arange(1,len(cum_f2)):
    cum_f2[i] = cum_f2[i] + cum_f2[i-1]
cum_f3 = np.copy(f3[:,4])
for i in np.arange(1,len(cum_f3)):
    cum_f3[i] = cum_f3[i] + cum_f3[i-1]
cum_f4 = np.copy(f4[:,4])
for i in np.arange(1,len(cum_f4)):
    cum_f4[i] = cum_f4[i] + cum_f4[i-1] 

#Plot flux
pl.figure()

fg = gridspec.GridSpec(4,1)
fg.update(hspace=0) 
up = pl.subplot(fg[0, :])
#pl.title('Dashed are with suppresion')
up.plot(f1[:,0],cum_f1/n1_bg_z,'r-',lw=1.5)
up.plot(f2[:,0],cum_f2/n2_bg_z,'b:',lw=2)
up.plot(f3[:,0],cum_f3/n3_bg_z,'g--',lw=2)
up.plot(f4[:,0],cum_f4/n4_bg_z,'m-.',lw=2)
up.plot(zov[0], cum_f1[y_pos0[0]]/n1_bg_z,'ro',markerfacecolor='None',markeredgecolor='r')
up.plot(zov[1], cum_f2[y_pos1[0]]/n2_bg_z,'ro',markerfacecolor='None',markeredgecolor='b')
up.plot(zov[2], cum_f3[y_pos2[0]]/n3_bg_z,'ro',markerfacecolor='None',markeredgecolor='g')
up.plot(zov[3], cum_f4[y_pos3[0]]/n4_bg_z,'ro',markerfacecolor='None',markeredgecolor='m')
up.set_ylabel('$N_{\\rm phot}/N_{\\rm atoms}$')
up.set_ylim([-0.2,2.5])
up.set_xlim([6,19.5])
up.minorticks_on()

factor1 = 100.**3
factor2 = 244.**3

factor = factor1/factor2
print factor
print 'here ',np.log10(f1[:,4][y_pos0[0]]*factor)#*(100/244)**3/1e70)

low = pl.subplot(fg[1:,:])
#low.plot(f1[:,0],np.log10(f1[:,3]/1e70),'r',label='no LMACHs')
#low.plot(f2[:,0],np.log10(f2[:,3]/1e70),'b',label='supp LMACHs')
#low.plot(f3[:,0],np.log10(f3[:,3]/1e70),'g',label='psupp LMACHs')
#low.plot(f4[:,0],np.log10(f4[:,3]/1e70),'m',label='gsupp LMACHs')
low.plot(f1[:,0],np.log10(f1[:,4]*100**3/244**3/1e70),'r-',lw=1.5,label='L1')
low.plot(f2[:,0],np.log10(f2[:,4]*100**3/244**3/1e70),'b:',lw=2,label='L2')
low.plot(f3[:,0],np.log10(f3[:,4]*100**3/244**3/1e70),'g--',lw=2,label='L3')
low.plot(f4[:,0],np.log10(f4[:,4]*100**3/244**3/1e70),'m-.',lw=2,label='L4')
low.plot(zov[0], np.log10(f1[:,4][y_pos0[0]]*(100./244.)**3/1e70),'ro',markerfacecolor='None',markeredgecolor='r')
low.plot(zov[1], np.log10(f2[:,4][y_pos1[0]]*(100./244.)**3/1e70),'ro',markerfacecolor='None',markeredgecolor='b')
low.plot(zov[2], np.log10(f3[:,4][y_pos2[0]]*(100./244.)**3/1e70),'ro',markerfacecolor='None',markeredgecolor='g')
low.plot(zov[3], np.log10(f4[:,4][y_pos3[0]]*(100./244.)**3/1e70),'ro',markerfacecolor='None',markeredgecolor='m')
#low.plot(f1[:,0],np.log10(f1[:,3]/1e70),'-',lw=0.5)
#low.plot(f2[:,0],np.log10(f2[:,3]/1e70),'k:',lw=1.5)
#low.plot(f3[:,0],np.log10(f3[:,3]/1e70),'g--',lw=2)
#low.plot(f4[:,0],np.log10(f4[:,3]/1e70),'k-.',lw=1.5)
low.set_ylim([-3.5,2.5])
low.set_ylabel('$\mathrm{log_{10}}(N_{\\rm phot}(L_{\\rm box,143})^{-3}/10^{70})$')
low.set_xlabel('$z$')
leg = low.legend(loc='lower left',prop={'size':12})
leg.draw_frame(False)
pl.xlim([6,19.5])
pl.setp(up.get_xticklabels(), visible=False)
pl.minorticks_on()
pl.show()
pl.savefig('../plot_python/png/244Mpc_250_flux_comb.png')
pl.savefig('../plot_python/eps/244Mpc_250_flux_comb.eps')
