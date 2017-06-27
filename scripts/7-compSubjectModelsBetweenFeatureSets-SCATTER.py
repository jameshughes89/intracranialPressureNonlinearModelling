'''
Does a scatter plot comparing the best from all featrues and the best from subset features. 

'''


import numpy as np
import csv
import matplotlib.pylab as plt
import scipy.stats


#subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']
linNonlin = ['', '_Linear']
feat = ['', '_lessFeatures']

allData = []
for fea in feat:
	for lnl in linNonlin:
		for tme in times:
			data =  np.array(list(csv.reader(open('3-abEmat' + lnl + '_' + tme + fea + '.csv', 'r')))).astype(float)
			allData.append(np.diagonal(data))

allData = np.array(allData)

cols = ['b','g','r']
for i in range(3):
	plt.scatter(allData[i], allData[i+6], color=cols[i], label=times[i])
	print np.nanmedian(allData[i]), '\n', np.nanmedian(allData[i+6]), '\n'
	print scipy.stats.mannwhitneyu(allData[i], allData[i+6])

plt.plot(range(0, 2, 1),color='k')
plt.xlim([0,1])
plt.ylim([0,1])
plt.title('Mean Absolute Error of Nonlinear Models Generated with All Features\n Against Models Generated with the Subset of Features')
plt.xlabel('All Features Mean Absolute Error')
plt.ylabel('Subset of Features Mean Absolute Error')
plt.legend()
plt.show()

