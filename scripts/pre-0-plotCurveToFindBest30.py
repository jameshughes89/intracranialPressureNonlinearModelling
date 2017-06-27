import csv
from math import *
import numpy as np
import scipy
import scipy.special
import matplotlib.pyplot as plt
import scipy.io
import scipy.signal
import sklearn
import sklearn.preprocessing

subs = [3002921, 3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3399093, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]

for s in subs:
	print s
	
	iFile = csv.reader(open('../oldPysioNet/PNdata/' + str(s) + '-all.csv','r'))


	v0 = []
	v1 = []
	v2 = []
	v3 = []
	v4 = []
	v5 = []
	v6 = []
	#v7 = []

	for l in iFile:
		v0.append(np.float64(l[0]))
		v1.append(np.float64(l[1]))
		v2.append(np.float64(l[2]))
		v3.append(np.float64(l[3]))
		v4.append(np.float64(l[4]))
		v5.append(np.float64(l[5]))
		v6.append(np.float64(l[6]))
		#v7.append(np.float64(l[7]))

	plt.plot(v0)
	plt.plot(v1)
	plt.plot(v2)
	plt.plot(v3)
	plt.plot(v4)
	plt.plot(v5)
	plt.plot(v6)

	plt.show()

#v0 --- RESP
#v1 --- PLETH
#v2 --- ECG-II
#v3 --- ECG-V
#v4 --- AVR
#v5 --- ABP
#v6 --- ICP
