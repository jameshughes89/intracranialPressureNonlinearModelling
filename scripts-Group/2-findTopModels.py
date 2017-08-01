'''
Finds the top model for each subject/task/take and saves them to a file bestExpression_TIME.txt
'''
import numpy as np
import csv
import sys

groups = ['0', '1', '2']
#subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']





for tme in times:
	allBestVal = []
	allBestInd = []
	bestExpressions = []
	for g in groups:
		print g, tme

		bestInd = -1;
		bestVal = sys.float_info.max
		iFile = csv.reader(open('../jGPv9-ICP/src/outs/' + g + '-' + tme + 'groupData/stats.csv', 'r'))
		
		for l in iFile:
			if float(l[1]) < bestVal:
				bestVal = float(l[1])
				bestInd = int(l[0])
		print '\t\t', bestInd, bestVal
		allBestVal.append(bestVal)
		allBestInd.append(bestInd)

		iFile = open('../jGPv9-ICP/src/outs/' + g + '-' + tme + 'groupData/' + str(allBestInd[-1]) + '_line.txt','r')
		bestExpressions.append(iFile.next())
		iFile.close()


			

	oFile = open('bestExpressions_' + tme + '.py','w')	
	oFile.write("from math import *\n\n")
	fs='funcs = ['
	count = 0
	for l in bestExpressions:
		oFile.write('def func_' + str(count) + '(v0,v1,v2,v3,v4,v5,v6): return ' + l + '\n')		#CHANGE HERE (in function name)
		fs = fs + "func_" + str(count)
		if count != len(bestExpressions) - 1:
			fs = fs + ","	

		count += 1

	fs = fs + "]"
	oFile.write("\n" + fs)

	oFile.write("\n\ndef getFuncs(): return funcs\n")
	oFile.close()

