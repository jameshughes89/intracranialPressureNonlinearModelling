'''
Generates a matrix showing which of the top models fit the best on all subject's data.
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import scipy.stats

#subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']



dataAll =  np.array(list(csv.reader(open('3-abEmat_all.csv', 'r')))).astype(np.float)
data250 =  np.array(list(csv.reader(open('3-abEmat_250.csv', 'r')))).astype(np.float)
data1s =  np.array(list(csv.reader(open('3-abEmat_1s.csv', 'r')))).astype(np.float)

dataAll_lessFeatures =  np.array(list(csv.reader(open('3-abEmat_all_lessFeatures.csv', 'r')))).astype(np.float)
data250_lessFeatures =  np.array(list(csv.reader(open('3-abEmat_250_lessFeatures.csv', 'r')))).astype(np.float)
data1s_lessFeatures =  np.array(list(csv.reader(open('3-abEmat_1s_lessFeatures.csv', 'r')))).astype(np.float)


bestMat = []

for i in range(dataAll.shape[0]):
	bestRow = []
	for j in range(dataAll.shape[1]):
		point = np.array([dataAll[i,j], data250[i,j], data1s[i,j],dataAll_lessFeatures[i,j], data250_lessFeatures[i,j], data1s_lessFeatures[i,j]])		
		if i == j:
			bestRow.append(np.float('nan'))
		elif np.isnan(np.min(point)):
			bestRow.append(np.float('nan'))
		else:
			bestRow.append(np.argmin(point))

	bestMat.append(bestRow)

bestMat = np.array(bestMat)

plt.matshow(bestMat)
plt.colorbar()
plt.show()

#countOfBest = np.bincount(np.digitize(stats[i], binz), minlength=len(binz))
#countOfBest = np.digitize(stats[i], binz)

forHist = bestMat[np.logical_not(np.isnan(bestMat))]
plt.hist(forHist.flatten())
plt.show()

binz = np.bincount(np.digitize(forHist, [1,2,3,4,5,6]))

plt.bar([0,1,2,3,4,5], binz)
plt.show()







#-#-#-#-#-#-#-#
# second part #
#-#-#-#-#-#-#-#
'''
same as above, but only with the 3 top models being compared.
'''

bestMat = []

for i in range(dataAll.shape[0]):
	bestRow = []
	for j in range(dataAll.shape[1]):
		point = np.array([dataAll[i,j],dataAll_lessFeatures[i,j], data250_lessFeatures[i,j]])		
		if i == j:
			bestRow.append(np.float('nan'))
		elif np.isnan(np.min(point)):
			bestRow.append(np.float('nan'))
		else:
			bestRow.append(np.argmin(point))

	bestMat.append(bestRow)

bestMat = np.array(bestMat)

plt.matshow(bestMat)
plt.colorbar()
plt.show()

#countOfBest = np.bincount(np.digitize(stats[i], binz), minlength=len(binz))
#countOfBest = np.digitize(stats[i], binz)

forHist = bestMat[np.logical_not(np.isnan(bestMat))]
plt.hist(forHist.flatten())
plt.show()

binz = np.bincount(np.digitize(forHist, [1,2,3]))

plt.bar([0,1,2], binz)
plt.show()


#-#-#-#-#-#-#-#
# Third  part #
#-#-#-#-#-#-#-#
'''
same as above, but only with the 2 top models being compared.
'''

bestMat = []

for i in range(dataAll.shape[0]):
	bestRow = []
	for j in range(dataAll.shape[1]):
		point = np.array([dataAll[i,j], data250_lessFeatures[i,j]])		
		if i == j:
			bestRow.append(np.float('nan'))
		elif np.isnan(np.min(point)):
			bestRow.append(np.float('nan'))
		else:
			bestRow.append(np.argmin(point))

	bestMat.append(bestRow)

bestMat = np.array(bestMat)

plt.matshow(bestMat)
plt.colorbar()
plt.show()

#countOfBest = np.bincount(np.digitize(stats[i], binz), minlength=len(binz))
#countOfBest = np.digitize(stats[i], binz)

forHist = bestMat[np.logical_not(np.isnan(bestMat))]
plt.hist(forHist.flatten())
plt.show()

binz = np.bincount(np.digitize(forHist, [1,2]))

plt.bar([0,1], binz)
plt.show()


flatDataAll = dataAll.flatten()
flatData250_lessFeatures = data250_lessFeatures.flatten()

plt.hist(flatDataAll, range=(0,20), bins=100, alpha=0.5, color='b')
plt.hist(flatData250_lessFeatures, range=(0,20), bins=100, alpha=0.5, color='g')
plt.axvline(np.median(flatDataAll), color='b', label=str(np.median(flatDataAll)))
plt.axvline(np.median(flatData250_lessFeatures), color='g', label=str(np.median(flatData250_lessFeatures)))
plt.legend()
plt.show()

plt.hist(flatDataAll, range=(0,5), bins=50, alpha=0.5, cumulative=True, color='b')
plt.hist(flatData250_lessFeatures, range=(0,5), bins=50, alpha=0.5, cumulative=True, color='g')
plt.axvline(np.median(flatDataAll), color='b', label=str(np.median(flatDataAll)))
plt.axvline(np.median(flatData250_lessFeatures), color='g', label=str(np.median(flatData250_lessFeatures)))
plt.legend()
plt.show()

print scipy.stats.mannwhitneyu(flatDataAll, flatData250_lessFeatures)




flatDataAll = dataAll.flatten()
flatData250_lessFeatures = data250_lessFeatures.flatten()
flatDataAll[flatDataAll > 1000] = sys.float_info.max
flatData250_lessFeatures[flatData250_lessFeatures > 1000] = sys.float_info.max

colors = []

countAllBetter = 0
count250_lessFeaturesCount = 0

accWorseFromAll = 0
accWorseFrom250_lessFeatures = 0
for i in range(len(flatDataAll)):
	if(flatDataAll[i] < flatData250_lessFeatures[i]):		# if all was better
		countAllBetter += 1
		colors.append('b')
		diff = flatData250_lessFeatures[i] - flatDataAll[i]
		if diff < 100000:
			accWorseFromAll += diff
	else:
		count250_lessFeaturesCount +=1
		colors.append('g')
		diff = flatDataAll[i] - flatData250_lessFeatures[i]
		if diff < 100000:
			accWorseFrom250_lessFeatures += diff

print "We added up how much 'worse' 250_less was from all whenever it was worse, it was:"
print accWorseFromAll
print "it was better than 250 this many times:"
print countAllBetter

print "We added up how much 'worse' all was from 250_less whenever it was worse, it was:"
print accWorseFrom250_lessFeatures
print "it was better than all this many times:"
print count250_lessFeaturesCount


#               x                     y
plt.scatter(flatDataAll, flatData250_lessFeatures, s=5, color=colors)
plt.plot([0,10],[0,10],color='k')
plt.ylim([0,10])
plt.xlim([0,10])
plt.show()


