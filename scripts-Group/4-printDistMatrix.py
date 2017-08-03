'''
prints the distance matrices based on script 3
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

#subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']


for tme in times:
	iFile =  csv.reader(open('3-abEmat_' + tme + '.csv', 'r'))

	abeMat = []
	for l in iFile:
		abeMat.append(l)
	abeMat = np.array(abeMat)
	abeMat = abeMat.astype(np.float)



	for i in range(len(abeMat)):
		for j in range(len(abeMat[i])):
			if abeMat[i][j] > 100:
				abeMat[i][j] = np.float('nan')
				#abeMat[i][j] = np.float(2)


	iFile =  csv.reader(open('3-msEmat_' + tme + '.csv', 'r'))
	mseMat = []
	for l in iFile:
		mseMat.append(l)
	mseMat = np.array(mseMat)
	mseMat = mseMat.astype(np.float)


	for i in range(len(mseMat)):
		for j in range(len(mseMat[i])):
			if mseMat[i][j] > 100 :
				mseMat[i][j] = np.float('nan')
				#mseMat[i][j] = np.float(2)


	iFile =  csv.reader(open('3-corrmat_' + tme + '.csv', 'r'))
	corrMat = []
	for l in iFile:
		corrMat.append(l)
	corrMat = np.array(corrMat)
	corrMat = corrMat.astype(np.float)

	'''
	for i in range(len(corrMat)):
		for j in range(len(corrMat[i])):
			if corrMat[i][j] > 100 :
				corrMat[i][j] = np.float('nan')
				#corrMat[i][j] = np.float(2)
	'''




	plt.matshow(np.log(abeMat), aspect='auto')
	plt.colorbar(label='Mean ABSOLUTE Error (log, and cut off anythong beyond 100)')
	plt.matshow(np.log(mseMat), aspect='auto')
	plt.colorbar(label='Mean SQUARED Error (log, and cut off anythong beyond 100)')	
	plt.matshow(corrMat, aspect='auto')
	plt.colorbar(label='Correlation')


	'''
	for i in range(30, 121, 30):
		plt.axvline(i - 0.5, color='k', linewidth=2)
		plt.axhline(i - 0.5, color='k', linewidth=2)

	for i in range(5, 151, 5):
		plt.axvline(i - 0.5, color='k', linewidth=1, linestyle='--')
		plt.axhline(i - 0.5, color='k', linewidth=1, linestyle='--')



	plt.title('Distance Matrix ' + TIME + ': Each Dataset Applied to All Models')
	plt.ylabel('Data',rotation=90)
	plt.xlabel('Model')
	plt.yticks(range(15,150, 30), tasks, rotation=90)
	plt.xticks(range(15,150, 30), tasks, rotation=0)
	'''
	#plt.colorbar(label='Mean Absolute Error (log, and cut off anythong beyond 100)')
	plt.show()



'''
# # #
# all in one big plot here
# # #

#plt.clf()

pltz = []

axes = plt.subplot2grid((1,3), (0,0))
pltz.append(axes)
img = pltz[0].matshow(abeMat)

for i in range(30, 121, 30):
	pltz[0].axvline(i - 0.5, color='k', linewidth=2)
	pltz[0].axhline(i - 0.5, color='k', linewidth=2)

for i in range(5, 151, 5):
	pltz[0].axvline(i - 0.5, color='k', linewidth=1, linestyle='--')
	pltz[0].axhline(i - 0.5, color='k', linewidth=1, linestyle='--')



pltz[0].set_title('Each Dataset Applied to All Models', fontsize=12)
pltz[0].set_ylabel('Data',rotation=90)
pltz[0].set_xlabel('Model')
pltz[0].set_yticks(range(15,150,30))
pltz[0].set_yticklabels(tasks, rotation=90)
pltz[0].set_xticks(range(15,150,30))
pltz[0].set_xticklabels(tasks, rotation=0)

divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(img, cax = cax)


axes = plt.subplot2grid((1,3), (0,1))
pltz.append(axes)
img = pltz[1].matshow(avgMat_TAKE)

for i in range(6, 30, 6):
	pltz[1].axvline(i - 0.5, color='k', linewidth=2)
	pltz[1].axhline(i - 0.5, color='k', linewidth=2)

for i in range(1, 30, 1):
	pltz[1].axvline(i - 0.5, color='k', linewidth=1, linestyle='--')
	pltz[1].axhline(i - 0.5, color='k', linewidth=1, linestyle='--')



pltz[1].set_title('Averaged Over Takes', fontsize=12)
#pltz[1].set_ylabel('Data',rotation=90)
pltz[1].set_xlabel('Model')
pltz[1].set_yticks(range(2,30,6))
pltz[1].set_yticklabels(tasks, rotation=90)
pltz[1].set_xticks(range(2,30,6))
pltz[1].set_xticklabels(tasks, rotation=0)
divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(img, cax = cax)

axes = plt.subplot2grid((1,3), (0,2))
pltz.append(axes)
img = pltz[2].matshow(avgMat_TASK)


for i in range(1, 6, 1):
	pltz[2].axvline(i - 0.5, color='k', linewidth=2)
	pltz[2].axhline(i - 0.5, color='k', linewidth=2)


pltz[2].set_title('Averaged Over Tasks', fontsize=12)
#pltz[2].set_ylabel('Data',rotation=90)
pltz[2].set_xlabel('Model')
pltz[2].set_yticks(range(0,5,1))
pltz[2].set_yticklabels(tasks, rotation=90)
pltz[2].set_xticks(range(0,5,1))
pltz[2].set_xticklabels(tasks, rotation=0)
divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(img, cax = cax, label='Mean Absolute Error (limited at 2)')
#plt.colorbar(img, label='Mean Absolute Error (limited at 2)')

#plt.colorbar(label='Mean Absolute Error (limited at 2)', cax=pltz[0])
#plt.tight_layout()
plt.suptitle('Error Matrix For All Data', fontsize=16)
plt.show()

'''
'''
'D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'
'''
