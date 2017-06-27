'''
Creates the statistics file for each subject/task/take. 

'''

import numpy as np
import csv

subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']

for sub in subjects:
	for tme in times:
		print sub, tme
		oFile = open('../jGPv9-ICP/src/outs/' + str(sub) + '-' + tme + '_lessFeatures/stats.csv', 'w')
		for i in range(0, 50, 1):
			iFile = open('../jGPv9-ICP/src/outs/' + str(sub) + '-' + tme + '_lessFeatures/' + str(i) + '_fit.txt', 'r')
			oFile.write(str(i)+","+iFile.read()+"\n")
		
		oFile.close()	

