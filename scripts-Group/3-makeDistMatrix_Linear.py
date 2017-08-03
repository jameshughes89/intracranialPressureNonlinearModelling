'''
Creates the error (or whatever metric we want to use) matrix when each model is applied to all data. It saves it to a file 3-metriCmat_TIME.csv
'''

import numpy as np
import csv
import sys
from math import *
import importlib

#groups = ['0', '1', '2']
subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']


for tme in times:
	bexp = importlib.import_module('bestLinearExpressions_' + tme, package=None)
	funcs = bexp.getFuncs()
	matrixMSE = []
	matrixABE = []
	matrixCorr = []
	count = 0

	for sub in subjects:
	
					
		print sub, tme, count
		count+= 1

		#this should be on the whole data
		iFile = csv.reader(open('../PNdata/' + str(sub) + '-' + 'all' + '.csv', 'r'))
		
		data = []

		for l in iFile:
			data.append(l)

		data = np.array(data)
		data = data.astype(np.float)
	
		allmsE = []
		allabE = []
		allCorr = []

		for f in funcs:
			#try:			
				msE = []
				abE = []
				allPred = []
				allExpected = []
				for l in data:
					try:
						pred = f(l[0],l[1],l[2],l[3],l[4],l[5],l[6])
						err = l[6] - pred
						
					except (OverflowError, ZeroDivisionError):
						err = np.float('nan')

					allPred.append(pred)
					allExpected.append(l[6])
					
					msE.append(err**2)
					abE.append(abs(err))
				
				allmsE.append((np.mean(msE)))
				allabE.append((np.mean(abE)))
				#allCorr.append(np.correlate(allPred, allExpected))
				crr = np.ma.corrcoef(allPred, allExpected)	
				allCorr.append(crr[0][1])
				#allmsE.append(log(np.mean(msE)))
				#allabE.append(log(np.mean(abE)))
				'''
				except OverflowError:
					print '\t\t\tBBBBBUSTTTEDDDD: ', sub, tme
					allmsE.append(np.float('nan'))
					allabE.append(np.float('nan'))
					allCorr.append(np.float('nan'))
					continue
				'''

		matrixMSE.append(allmsE)
		matrixABE.append(allabE)
		matrixCorr.append(allCorr)

	np.savetxt('3-msEmat_Linear_' + tme + '.csv', matrixMSE, delimiter=",")
	np.savetxt('3-abEmat_Linear_' + tme + '.csv', matrixABE, delimiter=",")
	np.savetxt('3-corrmat_Linear_' + tme + '.csv', matrixCorr, delimiter=",")


