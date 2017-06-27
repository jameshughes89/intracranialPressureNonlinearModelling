'''
Creates the accuracy when models were applied to the data fit to

does nonlinear all, nonoliear 250, nonlinear 1s, linear all, linear 250, linear 1s, nonlinear all less, etc. etc. etc. 

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
	plt.scatter(allData[i], allData[i+3], color=cols[i], label=times[i])
	print np.nanmedian(allData[i]), '\n', np.nanmedian(allData[i+3]), '\n'
	print scipy.stats.mannwhitneyu(allData[i], allData[i+3])

plt.plot(range(0, 2, 1),color='k')
plt.xlim([0,1])
plt.ylim([0,1])
plt.title('Mean Absolute Error of Nonlinear Models Against Linear Models')
plt.xlabel('Nonlinear Model Mean Absolute Error')
plt.ylabel('Linear Model Mean Absolute Error')
plt.legend()
plt.show()

print '\n\n\n\n'
for i in range(6,9,1):
	plt.scatter(allData[i], allData[i+3], color=cols[i-6], label=times[i-6])
	print np.nanmedian(allData[i]), '\n', np.nanmedian(allData[i+3]), '\n'
	print scipy.stats.mannwhitneyu(allData[i], allData[i+3])

plt.plot(range(0, 2, 1),color='k')
plt.xlim([0,1])
plt.ylim([0,1])
plt.title('Mean Absolute Error of Nonlinear Models Against Linear Models\nLess Features')
plt.xlabel('Nonlinear Model Mean Absolute Error')
plt.ylabel('Linear Model Mean Absolute Error')
plt.legend()
plt.show()


'''
# 250 less nonlin VS. all less lin
plt.scatter(allData[7], allData[9])
print np.nanmedian(allData[7]), '\n', np.nanmedian(allData[9]), '\n'
print scipy.stats.mannwhitneyu(allData[7], allData[9])
plt.plot(range(0, 2, 1),color='k')
plt.xlim([0,1])
plt.ylim([0,1])
plt.show()

'''
