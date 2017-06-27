'''
compares some curves for viz. 

'''

import numpy as np
import csv
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import scipy.stats
from math import *

# all
def func_all_nl(v0,v1,v2,v3,v4,v5,v6): return  ( v5 + ( ( v4 + (cos( v4 )- v3 ) ) / ( ( -4.713472306137936 + v5 ) / ( (cos( v4 )*cos( v4 )) - v4 ) ) ) ) 
def func_all_l(v0,v1,v2,v3,v4,v5,v6): return 0.0025049756407 * 1 + 0.0603568150366 * v0 + 0.0644263884501 * v1 + -1.63174124519 * v2 + -0.15291755434 * v3 + -1.64702848487 * v4 + 0.998643194313 * v5

# 250 
def func_250_nl(v0,v1,v2,v3,v4,v5,v6): return  ( ( (cos( v4 )/ ( ( v5 - v4 ) + -3.9794571039015523 ) ) - ( v2 + v4 ) ) + ( v5 + ( ( ( v2 + v4 ) * v2 ) / ( -3.9794571039015523 + v3 ) ) ) ) 
def func_250_l(v0,v1,v2,v3,v4,v5,v6): return -0.165388780354 * 1 + 0.0629225328269 * v0 + 0.0535493690433 * v1 + -1.84136164286 * v2 + -0.191104270981 * v3 + -1.81238355812 * v4 + 0.958115362935 * v5

# 1s
def func_1s_nl(v0,v1,v2,v3,v4,v5,v6): return  (sin( ( ( (abs(exp( v0 ))* -8.452600960917977 ) / ( ( ( -8.370353140292156 /abs(exp( v0 ))) -cos( -8.370353140292156 )) + (exp( v1 )*cos( v5 )) ) ) -exp( v0 )) )+sin( v5 ))
def func_1s_l(v0,v1,v2,v3,v4,v5,v6): return 0.0030724627399 * 1 + 0.299060691402 * v0 + 0.183569751115 * v1 + -3.35362484438 * v2 + -0.553834413797 * v3 + -2.97575418127 * v4 + 0.930863278691 * v5


# CHANGE THIS LINE IF YOU WANT TO GET ONLY 250, OR 1s VIEW OF WHAT THEY WERE TRAINED TO
data = np.array(list(csv.reader(open('../PNdata/3781713-all.csv', 'r')))).astype(float)	# !!!!!
# !!!!!!!!!!!!!


# all
real = []
predNL = []
predL = []

for l in data:
	real.append(l[-1])
	predNL.append(func_all_nl(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))
	predL.append(func_all_l(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))

pltz = []
axes = plt.subplot2grid((3,4), (0,0), colspan=4)
pltz.append(axes)

img = pltz[0].plot(real, label='Signal')
pltz[0].plot(predNL, label='Nonlinear')
pltz[0].plot(predL, label='Linear')
pltz[0].set_title('Fit to All Data', fontsize=12)
pltz[0].legend(fontsize=8)
#plt.show()



# 250
real = []
predNL = []
predL = []

for l in data:
	real.append(l[-1])
	predNL.append(func_250_nl(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))
	predL.append(func_250_l(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))

axes = plt.subplot2grid((3,4), (1,1), colspan=3)
pltz.append(axes)

img = pltz[1].plot(real, label='Signal')
pltz[1].plot(predNL, label='Nonlinear')
pltz[1].plot(predL, label='Linear')
pltz[1].set_title('Fit to 250 Data Points on All Data', fontsize=12)
#pltz[1].legend()




# 1s
real = []
predNL = []
predL = []

for l in data:
	real.append(l[-1])
	predNL.append(func_1s_nl(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))
	predL.append(func_1s_l(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))

axes = plt.subplot2grid((3,4), (2,1), colspan=3)
pltz.append(axes)

img = pltz[2].plot(real, label='Signal')
pltz[2].plot(predNL, label='Nonlinear')
pltz[2].plot(predL, label='Linear')
pltz[2].set_title('Fit to 1s of Data on All Data', fontsize=12)
pltz[2].set_xlabel('Time Point')

#pltz[2].legend()


# what fit to 250
data = np.array(list(csv.reader(open('../PNdata/3029993-250.csv', 'r')))).astype(float)	# !!!!!

real = []
predNL = []
predL = []

for l in data:
	real.append(l[-1])
	predNL.append(func_250_nl(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))
	predL.append(func_250_l(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))

axes = plt.subplot2grid((3,4), (1,0))
pltz.append(axes)

img = pltz[3].plot(real, label='Signal')
pltz[3].plot(predNL, label='Nonlinear')
pltz[3].plot(predL, label='Linear')
pltz[3].set_title('Fit to 250 Data Points', fontsize=12)

pltz[3].set_ylabel('Signal Intensity')

# what fit to 1s
data = np.array(list(csv.reader(open('../PNdata/3029993-1s.csv', 'r')))).astype(float)	# !!!!!

real = []
predNL = []
predL = []

for l in data:
	real.append(l[-1])
	predNL.append(func_1s_nl(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))
	predL.append(func_1s_l(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))

axes = plt.subplot2grid((3,4), (2,0))
pltz.append(axes)

img = pltz[4].plot(real, label='Signal')
pltz[4].plot(predNL, label='Nonlinear')
pltz[4].plot(predL, label='Linear')
pltz[4].set_title('Fit to 1s of Data', fontsize=12)



plt.show()

