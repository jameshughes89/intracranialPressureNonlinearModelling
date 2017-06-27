'''
Creates the accuracy when models were applied to the data fit to

does nonlinear all, nonoliear 250, nonlinear 1s, linear all, linear 250, linear 1s, nonlinear all less, etc. etc. etc. 

'''

import numpy as np
import csv
import matplotlib.pylab as plt
import scipy.stats


subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']
linNonlin = ['', '_Linear']
feat = ['', '_lessFeatures']

def calcCI(a):
	return scipy.stats.norm.interval(0.95, loc=np.nanmean(a), scale=(np.nanstd(a)/np.sqrt(len(a))))[1] - np.nanmean(a)	# return 1 because 0 is the negative

def calcIQR(a):
	# kill nans
	a = a[np.logical_not(np.isnan(a))]
	q75, q25 = np.percentile(a, [75 ,25])
	return q75-q25


nlData = []
lData = []

for tme in times:
	nlData.append(np.array(list(csv.reader(open('6-abEerrOfAllModels_' + tme + '.csv','r')))).astype(float))
	lData.append(np.diag(np.array(list(csv.reader(open('3-abEmat_Linear_' + tme + '.csv','r')))).astype(float)))

nlData = np.array(nlData)
lData = np.array(lData)


for i, sub in enumerate(subjects):
	print '\\hline', sub, '&', '%.4f'% np.nanmedian(nlData[0,i]), '(%.4f)'% calcIQR(nlData[0,i]), '&', '%.4f'% np.nanmin(nlData[0,i]), '&', '%.4f'% lData[0,i], '&', '%.4f'% np.nanmedian(nlData[1,i]), '(%.4f)'% calcIQR(nlData[1,i]), '&', '%.4f'% np.nanmin(nlData[1,i]), '&', '%.4f'% lData[1,i], '&', '%.4f'% np.nanmedian(nlData[2,i]), '(%.4f)'% calcIQR(nlData[2,i]), '&', '%.4f'% np.nanmin(nlData[2,i]), '&', '%.4f'% lData[2,i], '\\\\'



print '\n\n\n'

nlData = []
lData = []

for tme in times:
	nlData.append(np.array(list(csv.reader(open('6-abEerrOfAllModels_' + tme + '_lessFeatures.csv','r')))).astype(float))
	lData.append(np.diag(np.array(list(csv.reader(open('3-abEmat_Linear_' + tme + '_lessFeatures.csv','r')))).astype(float)))

nlData = np.array(nlData)
lData = np.array(lData)


for i, sub in enumerate(subjects):
	print '\\hline', sub, '&', '%.4f'% np.nanmedian(nlData[0,i]), '(%.4f)'% calcIQR(nlData[0,i]), '&', '%.4f'% np.nanmin(nlData[0,i]), '&', '%.4f'% lData[0,i], '&', '%.4f'% np.nanmedian(nlData[1,i]), '(%.4f)'% calcIQR(nlData[1,i]), '&', '%.4f'% np.nanmin(nlData[1,i]), '&', '%.4f'% lData[1,i], '&', '%.4f'% np.nanmedian(nlData[2,i]), '(%.4f)'% calcIQR(nlData[2,i]), '&', '%.4f'% np.nanmin(nlData[2,i]), '&', '%.4f'% lData[2,i], '\\\\'



