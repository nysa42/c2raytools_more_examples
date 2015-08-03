#This file illustrates some basic usage for the c2raytools package
#The script reads some data files and prints and plots some statistics

import c2raytools as c2t
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import scipy.interpolate

#Some path names. Modify these as needed
one_filename = './244_0_results/new2_rms_lc_244Mpc_0.dat'
two_filename =	'./244_8.2S_results/new2_rms_lc_244Mpc_8.2S.dat'
three_filename = './244_8.2pS_results/new2_rms_lc_244Mpc_8.2pS.dat'
four_filename = './244_gS_results/new2_rms_lc_244Mpc_gS.dat'
five_filename = './244_0_results/new2_rms_lcins_244Mpc_0.dat'
six_filename =	'./244_8.2S_results/new2_rms_lcins_244Mpc_8.2S.dat'
seven_filename = './244_8.2pS_results/new2_rms_lcins_244Mpc_8.2pS.dat'
eight_filename = './244_gS_results/new2_rms_lcins_244Mpc_gS.dat'

#Read in dTx files files (z, nu, dT_mean, dTconv_mean, dTconv_rms, dTconv_skew)
f1 = np.loadtxt(one_filename)
f2 = np.loadtxt(two_filename)
f3 = np.loadtxt(three_filename)
f4 = np.loadtxt(four_filename)
f5 = np.loadtxt(five_filename)
f6 = np.loadtxt(six_filename)
f7 = np.loadtxt(seven_filename)
f8 = np.loadtxt(eight_filename)

#Plot volume and mass neutral fractions
pl.figure()

#pl.subplot(221)
pl.plot(f1[:,1],f1[:,3],'r',label='244Mpc_f2_0_250')
pl.plot(f2[:,1],f2[:,3],'b',label='244Mpc_f2_8.2S_250')
pl.plot(f3[:,1],f3[:,3],'g',label='244Mpc_f2_8.2pS_250')
pl.plot(f4[:,1],f4[:,3],'m',label='244Mpc_f2_gS_250')
pl.ylim([0,10])
pl.xlim([210,70])
pl.title('Source comparison with lightcone effect')
pl.xlabel('v [MHz]')
pl.ylabel('$<\delta T_b>^{1/2}$ [mK]')
pl.legend(loc='upper right',prop={'size':11})
pl.savefig('dTrms_lc_raw_244_sources.png')

pl.clf()
pl.plot(f5[:,1],f5[:,3],'r',label='244Mpc_f2_0_250')
pl.plot(f6[:,1],f6[:,3],'b',label='244Mpc_f2_8.2S_250')
pl.plot(f7[:,1],f7[:,3],'g',label='244Mpc_f2_8.2pS_250')
pl.plot(f8[:,1],f8[:,3],'m',label='244Mpc_f2_gS_250')
pl.ylim([0,6])
pl.xlim([210,70])
pl.title('Source comparison with 5" beam, 0.4 MHz')
pl.xlabel('v [MHz]')
pl.ylabel('$<\delta T_b>^{1/2}$ [mK]')
pl.legend(loc='upper right',prop={'size':11})
pl.savefig('dTrms_lc_ins_244_sources.png')

'''
pl.clf()
pl.plot(nu1_bins,dTconv_rms1,'r',label='no LMACHs')
#pl.plot(nu1_bins,dTconv_rms1,'b',label='rms_conv_bw')
#pl.plot(f1[:,1],f1[:,4],'r--',label='conv')
pl.plot(nu2_bins,dTconv_rms2,'b',label='supp LMACHs')
pl.plot(nu3_bins,dTconv_rms3,'g',label='psupp LMACHs')
pl.plot(nu4_bins,dTconv_rms4,'m',label='gsupp LMACHs')
pl.ylim([0,8])
pl.xlim([210,70])
#pl.title('dT mean conv and not')
pl.xlabel('v [MHz]')
pl.ylabel('$<\delta T_b>^{1/2}$ [mK]')
pl.legend(loc='upper right',prop={'size':9})
pl.savefig('dTrms_convbw_244.png')



pl.clf()
pl.plot(nu1_bins,dTconv_rms1,'r',label='no LMACHs')
#pl.plot(nu1_bins,dTconv_rms1,'b',label='rms_conv_bw')
#pl.plot(f1[:,1],f1[:,4],'r--',label='conv')
pl.plot(nu2_bins,dTconv_rms2,'b',label='supp `lMACHs')
pl.plot(nu3_bins,dTconv_rms3,'g',label='psupp LMACHs')
pl.plot(nu4_bins,dTconv_rms4,'m',label='gsupp LMACHs')
pl.ylim([-5,15])
pl.xlim([210,70])
#pl.title('dT mean conv and not')
pl.xlabel('v [MHz]')
pl.ylabel('$<\delta T_b>^{1/2}$ [mK]')
pl.legend(loc='upper right',prop={'size':9})
pl.savefig('dTskew_convbw_244.png')

pl.clf()
#pl.subplot(222)
pl.plot(f1[:,1],f1[:,5],'r',f2[:,1],f2[:,5],'b',f3[:,1],f3[:,5],'g',f4[:,1],f4[:,5],'m')
#pl.xlim([6,13]
pl.xlim([210,80])
#pl.title('dT rms conv and not')
pl.xlabel('v [MHz]', fontsize=14)
pl.ylabel('$<\delta T_b>^{1/2}$ [mK]', fontsize=14)
pl.legend(loc='lower right',prop={'size':10})
pl.savefig('rmsconv_244Mpc.png')

#pl.clf()
#pl.plot(f1[:,1],f1[:,5],'ro',label='no LMACHs')
#pl.plot(f2[:,1],f2[:,5],'bo',label='supp LMACHs')
#pl.plot(f1[:,1],crfit1,'r-',label='fit')
#pl.plot(f2[:,1],crfit2,'b-',label='fit supp')
#pl.plot(f3[:,0],f3[:,1],'g',label='psupp LMACHs')
#pl.plot(f4[:,0],f4[:,1],'Indigo',label='gsupp LMACHs')
#pl.xlim([6,13])
#pl.xlim([210,80])
#pl.title('rms nu fit')
#pl.xlabel('nu')
#pl.ylabel('rms')
#pl.legend(loc='upper right',prop={'size':9})
#pl.savefig('dTsplinetest_244Mpc.png')'''

#pl.subplot(223)
#pl.semilogy(f1[:,0],f1[:,1],'r',f2[:,0],f2[:,1],'b',f3[:,0],f3[:,1],'g',f4[:,0],f4[:,1],'Indigo')
#pl.xlim([6,17])
#pl.ylim([1e-4,1])
#pl.title('Volume-weighted')
#pl.xlabel('z')
#pl.ylabel('x')

#pl.subplot(224)
#pl.semilogy(f1[:,0],f1[:,2],'r',f2[:,0],f2[:,2],'b',f3[:,0],f3[:,2],'g',f4[:,0],f4[:,2],'Indigo')
#pl.xlim([6,17])
#pl.ylim([1e-4,1])
#pl.title('Mass-weighted')
#pl.xlabel('z')
#pl.ylabel('x')

#pl.ylim([1e-4,1])
#pl.savefig('xfrac_47Mpc_306.png')

'''nu = f1[:,1]
nu_right = np.zeros(len(f1[:,1]))
nu_width = np.zeros(len(f1[:,1]))
for i in range(0,len(f1[:,1])-1):
    if i == len(f1[:,1])-1:
        nu_right[i] = nu[i] + 0.5*(nu[i] - nu[i-1])
    elif i == 0:
        nu_right[i] = nu[i] + 0.5*(nu[i+1] - nu[i])
        nu_width[i] = 2*(nu_right[i] - nu[i])
    else:    
        nu_right[i] = nu[i] + 0.5*(nu[i+1] - nu[i])
        nu_width[i] = nu_right[i] - nu_right[i-1]

dnu = 0.2
nu_range = max(nu) - min(nu) + dnu
nu_bins = np.zeros(np.ceil(nu_range/dnu))
for i in range(0,len(nu_bins)):
    nu_bins[i] = nu[0] + i*dnu
    #print nu[0],nu_bins[i]
#print nu_bins

rms_conv1 = f1[:,5]
rms_bw1 = np.zeros(len(nu_bins))
i = 0
j = 0
nu_now = nu_bins[0] - dnu/2 - dnu/1000
#print nu_bins[0], nu_bins[0] + dnu/2, nu_bins[0] - dnu/2
while i < len(nu_bins) and j < len(nu):
    print 'i,j = ',i,j
    #print 'start at ',i,j,rms_conv1[j],rms_bw1[i]/dnu,rms_bw1[i+1]/dnu
    while nu_now < nu_bins[i] + dnu/2:
        nu_now += dnu
        if j >= len(nu): break
        #print nu_now, nu_bins[i] + dnu/2
        if nu_now > nu_bins[i] + dnu/2:
            #print 'case 1a',i,j,rms_bw1[i]/dnu
            rms_bw1[i] += rms_conv1[j]*(nu_bins[i] + dnu/2 - nu_now + dnu)
            nu_now = nu_bins[i] + dnu/2
            #print 'case 1',i,j,rms_bw1[i]/dnu
            i+=1
            break
        elif nu_now < nu_right[j]:
            #print 'case 2a',i,j,rms_bw1[i]/dnu
            rms_bw1[i] += rms_conv1[j]*dnu
            #print 'case 2',i,j,rms_bw1[i]/dnu
            i+=1
            break
        else:
            #print 'case 3a',i,j,rms_bw1[i]/dnu
            rms_bw1[i] += rms_conv1[j]*(nu_right[j] - nu_now + dnu)
            nu_now = nu_right[j]
            #print 'case 3',i,j,rms_bw1[i]/dnu
            j+=1
            break
print rms_bw1/dnu
      
#    if nu_bins[i] + i*dnu/2 <= nu_right[j]:
#        #print 'nu_right,bins = %.3f, %.3f',nu_right[j],nu_bins[i]
#        rms_bw1[i] += rms_conv1[j]*dnu
#        print i,j,rms_bw1[i]/dnu
        #j += 1
#        continue
#    elif nu_bins[i] + i*dnu/2 > nu_right[j]:
#        print (nu_bins[i] + i*dnu/2 - nu_right[j])
#        if nu_bins[i] + i*dnu/2 <= nu_right[j+1]:
            rms_bw1[i] += rms_conv1[j]*(nu_right[j] - nu_bins[i] + i*dnu/2)
            rms_bw1[i] += rms_conv1[j+1]*(nu_right[j] - nu_bins[i] + i*dnu/2 )
        elif nu_bins[i] + i*dnu/2 > nu_right[j]:
            rms_bw1[i+1] += rms_conv1[j]*(nu_right[j] - nu_bins[i] - i*dnu/2)
        print i,j,rms_bw1[i]/dnu
        print 'next',rms_bw1[i]/dnu
        j += 1
        continue 
    while nu_right[j] <= nu_bins[i] + i*dnu/2:
        print 'j = ',j
        #print 'nu_right,bin = %.3f, %.3f',nu_right[i],nu_bins[i]
        rms_bw1[i] = rms_bw1[i] + rms_conv1[j]*nu_width[j]
        j += 1
        print i,j,rms_bw1[i]/dnu
        if j == len(nu_right): break
    if j == len(nu_right): break
    rms_bw1[i] = rms_bw1[i] + rms_conv1[j]*(nu_bins[i] + i*dnu/2 - nu_right[j-1])
    rms_bw1[i+1] = rms_bw1[i+1] + rms_conv1[j]*(nu_right[j] - nu_bins[i] - i*dnu/2)
    j += 1
    print rms_bw1[i]/dnu
rms_bw1 /= dnu
nicerms = ["%.4f" % v for v in rms_bw1]
#print nicerms
'''
