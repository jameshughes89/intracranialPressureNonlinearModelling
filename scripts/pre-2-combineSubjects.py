'''
Combines the subject files into large data files. 

There will be 3 in total (so 10 subjects/file)

This is being done to see if I can have a more general model. 

'''

import numpy as np
import csv

subGroup = [[3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177], [3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360], [3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]]
times = ['all','250','1s']


for i, subjects in enumerate(subGroup):
	for tme in times:
		print i, tme
		#oFile = open('../PNdata/' + str(i) + '-' + tme + 'groupData.csv', 'a')
		#allDat = np.array([]*7)
		for sub in subjects:
			data = np.array(list(csv.reader(open('../PNdata/' + str(sub) + '-' + tme + '.csv', 'r')))).astype(float)
			np.savetxt(open('../PNdata/' + str(i) + '-' + tme + 'groupData.csv', 'a+'), data, delimiter=',', )
		
	

