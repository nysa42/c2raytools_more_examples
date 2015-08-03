# PURPOSE: Program to calculate the ionized fraction (by volume and mass) and store into a file
# INPUT:   The density and xfrac files from C2Ray and a redshift file
# OUTPUT:  A txt file with z, iof_vol, and iof_mass
# USAGE:   Be sure to set the paths, names, and mesh appropriately
# AUTHOR:  Keri L. Dixon 17.06.2014

import c2raytools as c2t
import numpy as np
#import array as ar

#Filename
xfrac_filename = './results/xfrac_244Mpc_f2_8.2S_250.dat'
out_filename =	'./results/tau_244Mpc_f2_8.2S_250.dat'

#Read in xfrac file created with fractions.py, creating a three column array with z, ion_vol, ion_mass
xfrac_data = np.loadtxt(xfrac_filename)

#Put into arrays to fit older code
#for f in xfrac_data:
#z = np.array([f[0] for f in xfrac_data])
#iof_vol = np.array([f[1] for f in xfrac_data])
#iof_mass = np.array([f[2] for f in xfrac_data])
z = np.array(xfrac_data[:,0])
z = z[::-1]
iof_mass = np.array(xfrac_data[:,2])
iof_mass = iof_mass[::-1]


#Calculate tau and put into file and plot or not
tau0, tau_z = c2t.tau(iof_mass, z)
print tau_z
print tau0
tau_array = np.column_stack((tau_z,tau0))

np.savetxt(out_filename, tau_array, delimiter=" ", fmt='%.3f %.4e')

	

  
