'''
Makes histograms to compare ALL models for ALL subjects between models made with all features and those made with the smaller set. 
'''

import numpy as np
import csv
import sys
import matplotlib.pylab as plt

subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']



for tme in times:

	#for sub in subjects:
	#	print sub, tme

	stats = (np.array(list(csv.reader(open('6-abEerrOfAllModels_' + tme +'.csv','r')))).astype(np.float).flatten())
	stats_lessFeatures = (np.array(list(csv.reader(open('6-abEerrOfAllModels_' + tme +'_lessFeatures.csv','r')))).astype(np.float).flatten())
	

	stats = np.array(stats)
	stats[stats>100] =np.float('nan')
	stats = stats[np.logical_not(np.isnan(stats))]
	stats_lessFeatures[stats_lessFeatures>100] =np.float('nan')
	stats_lessFeatures = np.array(stats_lessFeatures)
	stats_lessFeatures = stats_lessFeatures[np.logical_not(np.isnan(stats_lessFeatures))]

	plt.hist(stats, bins=100, alpha=0.5)
	plt.hist(stats_lessFeatures, bins=100, alpha=0.5)
	plt.show()
