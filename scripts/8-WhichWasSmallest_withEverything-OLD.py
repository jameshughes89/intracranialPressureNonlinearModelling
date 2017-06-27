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


dataLinearAll =  np.array(list(csv.reader(open('3-abEmat_Linear_all.csv', 'r')))).astype(np.float)
dataLinear250 =  np.array(list(csv.reader(open('3-abEmat_Linear_250.csv', 'r')))).astype(np.float)
dataLinear1s =  np.array(list(csv.reader(open('3-abEmat_Linear_1s.csv', 'r')))).astype(np.float)

dataLinearAll_lessFeatures =  np.array(list(csv.reader(open('3-abEmat_Linear_all_lessFeatures.csv', 'r')))).astype(np.float)
dataLinear250_lessFeatures =  np.array(list(csv.reader(open('3-abEmat_Linear_250_lessFeatures.csv', 'r')))).astype(np.float)
dataLinear1s_lessFeatures =  np.array(list(csv.reader(open('3-abEmat_Linear_1s_lessFeatures.csv', 'r')))).astype(np.float)




bestMat = []

for i in range(dataAll.shape[0]):
	bestRow = []
	for j in range(dataAll.shape[1]):
		point = np.array([dataAll[i,j], data250[i,j], data1s[i,j],dataAll_lessFeatures[i,j], data250_lessFeatures[i,j], data1s_lessFeatures[i,j], dataLinearAll[i,j], dataLinear250[i,j], dataLinear1s[i,j],dataLinearAll_lessFeatures[i,j], dataLinear250_lessFeatures[i,j], dataLinear1s_lessFeatures[i,j]])		
		if i == j:
			bestRow.append(np.float('nan'))
		elif np.isnan(np.nanmin(point)):
			bestRow.append(np.float('nan'))
			print point
		else:
			bestRow.append(np.nanargmin(point))

	bestMat.append(bestRow)

bestMat = np.array(bestMat)

plt.matshow(bestMat)
plt.colorbar()
plt.show()

#countOfBest = np.bincount(np.digitize(stats[i], binz), minlength=len(binz))
#countOfBest = np.digitize(stats[i], binz)

forHist = bestMat[np.logical_not(np.isnan(bestMat))]


binz = np.bincount(np.digitize(forHist, [1,2,3,4,5,6,7,8,9,10,11,12]))

plt.bar([0,1,2,3,4,5,6,7,8,9,10,11], binz)
plt.xticks([1.5,4.5,7.5,10.5], ['all features NL', 'subset features NL', 'all features L', 'subset features L'])
plt.ylabel('# times a model was the best when aplied to everyones data')
plt.xlabel('order --- Trained on all data points, 250 data points, 1s worth of data points')
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
		point = np.array([dataAll[i,j], data250_lessFeatures[i,j],dataLinearAll_lessFeatures[i,j]])		
		if i == j:
			bestRow.append(np.float('nan'))
		elif np.isnan(np.nanmin(point)):
			bestRow.append(np.float('nan'))
			print point
		else:
			bestRow.append(np.nanargmin(point))

	bestMat.append(bestRow)

bestMat = np.array(bestMat)

plt.matshow(bestMat)
plt.colorbar()
plt.show()

#countOfBest = np.bincount(np.digitize(stats[i], binz), minlength=len(binz))
#countOfBest = np.digitize(stats[i], binz)

forHist = bestMat[np.logical_not(np.isnan(bestMat))]


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
		point = np.array([data250_lessFeatures[i,j],dataLinearAll_lessFeatures[i,j]])		
		if i == j:
			bestRow.append(np.float('nan'))
		elif np.isnan(np.nanmin(point)):
			bestRow.append(np.float('nan'))
			print point
		else:
			bestRow.append(np.nanargmin(point))

	bestMat.append(bestRow)

bestMat = np.array(bestMat)

plt.matshow(bestMat)
plt.colorbar()
plt.show()

#countOfBest = np.bincount(np.digitize(stats[i], binz), minlength=len(binz))
#countOfBest = np.digitize(stats[i], binz)

forHist = bestMat[np.logical_not(np.isnan(bestMat))]


binz = np.bincount(np.digitize(forHist, [1,2]))

plt.bar([0,1], binz)
plt.show()

for i in range(len(dataLinearAll_lessFeatures)):
	dataLinearAll_lessFeatures[i,i] = sys.float_info.max
	data250_lessFeatures[i,i] = sys.float_info.max

flatDataAll = dataLinearAll_lessFeatures.flatten()
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



for i in range(len(dataLinearAll_lessFeatures)):
	dataLinearAll_lessFeatures[i,i] = sys.float_info.max
	data250_lessFeatures[i,i] = sys.float_info.max

flatDataAll = dataLinearAll_lessFeatures.flatten()
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
print 'sum of how much worse divided by how many times 250 was worse:'
print accWorseFromAll/countAllBetter

print "We added up how much 'worse' all was from 250_less whenever it was worse, it was:"
print accWorseFrom250_lessFeatures
print "it was better than all this many times:"
print count250_lessFeaturesCount
print 'sum of how much worse divided by how many times all was worse:'
print accWorseFrom250_lessFeatures/count250_lessFeaturesCount


#               x                     y
plt.scatter(flatDataAll, flatData250_lessFeatures, s=5, color=colors)
plt.plot([0,10],[0,10],color='k')
plt.ylim([0,2])
plt.xlim([0,2])
plt.show()


