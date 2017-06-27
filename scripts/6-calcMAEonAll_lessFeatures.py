'''
Creates the error (or whatever metric we want to use) matrix when each model is applied to all data. It saves it to a file 3-metriCmat_TIME.csv
'''

import numpy as np
import csv
import sys
from math import *
import importlib

subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']


for tme in times:
	bexp = importlib.import_module('allExpressions_' + tme + '_lessFeatures', package=None)
	funcs = bexp.getFuncs()

	matrixABE = []


	count = 0
	for sub in subjects:		
		print sub, tme

		#this should be on the whole data
		iFile = csv.reader(open('../PNdata/' + str(sub) + '-' + 'all' + '_lessFeatures.csv', 'r'))
		
		data = []

		for l in iFile:
			data.append(l)

		data = np.array(data)
		data = data.astype(np.float)
	
		allabE = []

		for f in funcs[count]:
			abE = []
			for l in data:
				try:
					pred = f(l[0],l[1],l[2],l[3])
					err = l[3] - pred
				except (OverflowError, ZeroDivisionError, ValueError):
					err = np.float('nan')
			
				abE.append(abs(err))
			allabE.append((np.mean(abE)))


		matrixABE.append(allabE)
		count+=1

	matrixABE = np.array(matrixABE)
	np.savetxt('6-abEerrOfAllModels_' + tme + '_lessFeatures.csv', matrixABE, delimiter=",")
	np.savetxt('6-abEerrOfAllModels-NoNaN_' + tme + '_lessFeatures.csv', matrixABE[np.logical_not(np.isnan(matrixABE))], delimiter=",")



