'''
Gets all models and makes them python-ie and saves them to a file allExpression_TIME.txt
'''
import numpy as np
import csv
import sys

subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']





for tme in times:


	oFile = open('allExpressions_' + tme + '.py','w')	
	oFile.write("from math import *\n\n")
	fs = 'funcs = ['

	for sub in subjects:
		
		fsSub = 'funcs' + str(sub) + ' = ['
		print sub, tme
		for i in range(50):
			iFile = open('../jGPv9-ICP/src/outs/' + str(sub) + '-' + tme + '/' + str(i) + '_line.txt','r')

			oFile.write('def func_' + str(sub) + '_' + str(i) + '(v0,v1,v2,v3,v4,v5,v6): return ' + iFile.next() + '\n')
			iFile.close()

			fsSub = fsSub + 'func_' + str(sub) + '_' + str(i)
			if i != 49:		# HARD coded this
				fsSub = fsSub + ','	

		fsSub = fsSub + ']\n\n'
		oFile.write("\n" + fsSub)
		fs = fs + 'funcs' + str(sub) + ','


	fs = fs + ']'

	oFile.write("\n" + fs)

	oFile.write("\n\ndef getFuncs(): return funcs\n")
	oFile.close()

