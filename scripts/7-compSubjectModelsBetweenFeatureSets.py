'''
Makes histograms to compare models for EACH subjects between models made with all features and those made with the smaller set. \

JAMES:
		TURN THIS INTO A VIOLIN PLOT!

		http://matplotlib.org/examples/statistics/violinplot_demo.html

'''

import numpy as np
import csv
import sys
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import sklearn.preprocessing
import scipy.stats

subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']


for tme in times:
	diffArray = []
	binz = np.arange(0,2,0.02)
	pValz = []


	stats = np.array(list(csv.reader(open('6-abEerrOfAllModels_' + tme +'.csv','r')))).astype(np.float)
	stats_lessFeatures = np.array(list(csv.reader(open('6-abEerrOfAllModels_' + tme +'_lessFeatures.csv','r')))).astype(np.float)

	stats = np.array(stats)
	stats[stats>100] =np.float('nan')
#	stats = stats[np.logical_not(np.isnan(stats))]
	stats_lessFeatures[stats_lessFeatures>100] =np.float('nan')
	stats_lessFeatures = np.array(stats_lessFeatures)
#	stats_lessFeatures = stats_lessFeatures[np.logical_not(np.isnan(stats_lessFeatures))]

	digAllList = []
	digLessList = []	
	for i, sub in enumerate(subjects):
		print sub, tme

			
		print '\t\t\tmed stats', np.median(stats[i]), '\t\t\tmed statsLess', np.median(stats_lessFeatures[i])
		print '\t\t\t\t\t\t\t\t\tp-val', scipy.stats.mannwhitneyu(stats[i], stats_lessFeatures[i])[1]
		pValz.append(scipy.stats.mannwhitneyu(stats[i], stats_lessFeatures[i])[1])
		digAll = np.bincount(np.digitize(stats[i], binz), minlength=len(binz))
		if len(digAll) > len(binz):
			digAll = digAll[:-1]
		digAllList.append(digAll)


		digLess = np.bincount(np.digitize(stats_lessFeatures[i], binz), minlength=len(binz))
		if len(digLess) > len(binz):
			digLess = digLess[:-1]
		digLessList.append(digLess)


		diffDig = digAll - digLess
		normDiffDig = sklearn.preprocessing.normalize(diffDig)[0]

		diffArray.append(normDiffDig)


	#plt.matshow(diffArray, aspect='auto')
	#plt.yticks(range(0,30,1), pValz)
	#plt.xticks(range(0, len(binz), 5), binz[::5])
	#plt.title(tme)
	#plt.colorbar(label='All Features - Less Features')
#plt.show()

'''
This bit does the violin plot part. Good luck!
'''

stats2 = []
stats_lessFeatures2 = []
for i in range(len(stats)):
	stats2.append(stats[i][np.logical_not(np.isnan(stats[i]))])
	stats_lessFeatures2.append(stats_lessFeatures[i][np.logical_not(np.isnan(stats_lessFeatures[i]))])

#stats = stats[np.logical_not(np.isnan(stats))]



pltz = []
count = 0
for tme in times:
	# add lines
	#for i in range(2,60,2):
	#	plt.axhline(i+0.5, c='k', linestyle=':')

	# do the filling in bit

	axes = plt.subplot2grid((1,3), (0,count))
	pltz.append(axes)



	for i in range(5,120,8):
		pltz[count].fill_between(range(0,4,1), i+0.5, i-4+0.5, color = '0.90')

	partz = pltz[count].violinplot(stats2, positions=range(120,0,-4), vert=False, showmedians=True, showextrema=False)
	for pc in partz['bodies']:
		pc.set_facecolor('b')
		pc.set_edgecolor('k')
		#pc.set_color('b')


	partz = pltz[count].violinplot(stats_lessFeatures2, positions=range(119,0,-4), vert=False, showmedians=True, showextrema=False)
	for pc in partz['bodies']:
		pc.set_facecolor('g')
		pc.set_edgecolor('k')

	pltz[count].set_xlim([0,2])
	pltz[count].set_ylim([0,121])
	pltz[count].set_title(tme)
	#pltz[count].set_xlabel('Mean Absolute Error')



	
	count+=1

pltz[1].set_xlabel('Mean Absoulte Error')
pltz[0].set_ylabel('Subject')
pltz[0].set_yticks(range(0+3,120+3,4))
pltz[0].set_yticklabels(subjects[::-1])
pltz[1].set_yticks([])
pltz[2].set_yticks([])

plt.suptitle('Distributions of Models Fit to All Features\nand Models Fit to Subset of Features', fontsize=16)
plt.show()

