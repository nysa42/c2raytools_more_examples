#This file illustrates some basic usage for the c2raytools package
#The script reads some data files and prints and plots some statistics

import numpy as np

#Some path names. Modify these as needed
in_filename = './results/xfrac_244Mpc_f2_8.2S_250.dat'
out_filename =	'./red_short.dat'

#Read in xfrac file
f1 = np.loadtxt(in_filename)

out = open(out_filename, 'w')

f1xm = f1[:,2]
z1 = f1[:,0]
i = 0
while f1xm[i] < 0.10: i+=1
if abs(f1xm[i]-0.1) < abs(f1xm[i-1]-0.1):
    print 'f1xm at 10% at z=', z1[i]
    out.write('%.3f\n' % z1[i])
else:
    print 'prev f1xm at 10% at z=', z1[i-1]
    out.write('%.3f\n' % z1[i-1])

while f1xm[i] < 0.30: i+=1
if abs(f1xm[i]-0.3) < abs(f1xm[i-1]-0.3):
    print 'f1xm at 30% at z=', z1[i]
    out.write('%.3f\n' % z1[i])
else:
    print 'prev f1xm at 30% at z=', z1[i-1]    
    out.write('%.3f\n' % z1[i-1])
    
while f1xm[i] < 0.50: i+=1
if abs(f1xm[i]-0.5) < abs(f1xm[i-1]-0.5):
    print 'f1xm at 50% at z=', z1[i]
    out.write('%.3f\n' % z1[i])
else:
    print 'prev f1xm at 50% at z=', z1[i-1]
    out.write('%.3f\n' % z1[i-1])
    
while f1xm[i] < 0.70: i+=1
if abs(f1xm[i]-0.7) < abs(f1xm[i-1]-0.7):
    print 'f1xm at 70% at z=', z1[i]
    out.write('%.3f\n' % z1[i])
else:
    print 'prev f1xm at 70% at z=', z1[i-1]
    out.write('%.3f\n' % z1[i-1])
    
while f1xm[i] < 0.90: i+=1
if abs(f1xm[i]-0.9) < abs(f1xm[i-1]-0.9):
    print 'f1xm at 90% at z=', z1[i]
    out.write('%.3f\n' % z1[i])
else:
    print 'prev f1xm at 90% at z=', z1[i-1]
    out.write('%.3f\n' % z1[i-1])
out.close()
