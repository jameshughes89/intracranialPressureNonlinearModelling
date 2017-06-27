import csv
import numpy as np



subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']

for tme in times:
	for s in subjects:
		print s
		data = []
	
		iFile = csv.reader(open('../PNdata/' + str(s) + '-' + tme + '.csv','r'))
	
		for r in iFile:
			data.append(r)
		data = np.array(data).astype(float)
		data = data[:,[1,3,5,6]]
		np.savetxt('../PNdata/' + str(s) + '-' + tme + '_lessFeatures.csv', data, delimiter=',')

