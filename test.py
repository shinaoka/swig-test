#import alps.hdf5
#import alps.gf
#
#a = alps.hdf5.archive()
#a.open('input.out.h5', 'r')
#N_mesh = -1
#a.read('/gtau_removal/mesh/N', N_mesh)
#print(N_mesh)

#g = alps.gf.legendre_gf(alps.gf.legendre_mesh())
#alps.gf.load('A.h5')
import numpy as np
import example

print example.drms(np.array([0.2, 0.1]))
print example.crms(1J*np.array([0.0, 0.1]))
