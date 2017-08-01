'''
Counts the number of times each variable was in all of the generated models. 
'''

import numpy as np
import csv
import sys
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

groups = ['0', '1', '2']
#subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']


dimensions=['RES', 'PLETH', 'ECG-II', 'ECG-V', 'ECG-AVR', 'ABP', 'ICP']

allBestVal = []
allBestInd = []
allmsE = []
allabE = []

allVarCounts = []

pltz = []
count = 0
for tme in times:
	allBestVal = []
	allBestInd = []
	allmsE = []
	allabE = []

	allVarCounts = []
	for g in groups:
		print g, tme
		fcount = np.zeros(len(dimensions))
		for i in range(50):
			iFile = csv.reader(open('../jGPv9-ICP/src/outs/' + g + '-' + tme + 'groupData/' + str(i) + '_multi.txt','r'), delimiter='\t')
			fBool = [False] * 7		
			for line in iFile:
				if(line[-1][0] == 'v'):
					eInt = int(line[-1][1:])
			
					if(not(fBool[eInt])):
						fBool[eInt] = True
						fcount[eInt] += 1


		fcount[-1] = 50
		allVarCounts.append(fcount)


	allVarCounts = np.array(allVarCounts).astype(float)
	allVarCounts = allVarCounts/50
	print np.mean(allVarCounts, axis=0)
	
	
	axes = plt.subplot2grid((1,3), (0,count))
	pltz.append(axes)
	img = pltz[count].matshow(allVarCounts.T, aspect='auto')
	#plt.colorbar(label='% Models Containing Feature')
	divider = make_axes_locatable(axes)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	if count != 2:
		cbar = plt.colorbar(img, cax = cax)	
	else:
		cbar = plt.colorbar(img, cax = cax, label='% Models Containing Feature')

	pltz[count].set_title(tme)

	pltz[count].set_xticks([])
	#pltz[count].set_xticks(range(len(subjects)))
	#pltz[count].set_xticklabels(subjects, rotation=90)
	#for i in range(len(tasks)):
	#	plt.axhline(i*len(subjects)*len(takes)-1, color='k', linewidth=2.0)

	#for i in range(4,150,5):
	#	plt.axhline(i, color='k', linewidth=1.0, linestyle='--')


	pltz[count].set_yticks([])

	for i in range(0, len(dimensions), 1):
		pltz[count].axhline(i-.5, color='k', linewidth=2.0)
	#plt.show()
	count+=1

pltz[0].set_ylabel('Device')
pltz[0].set_yticks(range(len(dimensions)))
pltz[0].set_yticklabels(dimensions,rotation=0)

pltz[1].set_xlabel('Group')

plt.suptitle('Features Present in Models', fontsize=16)
plt.show()

'''
# # # #
# TRANSPOSED VERSION  
# # # #

plt.matshow(allVarCounts.T, aspect='auto')
plt.colorbar(label='% Models Containing Feature')
plt.title('Features When Trained on ' + TIME + ' of the Data')
plt.xlabel('Subjects and Tasks')
plt.xticks(range(15,150, 30), tasks)
for i in range(len(tasks)):
	plt.axvline(i*len(subjects)*len(takes)-0.5, color='k', linewidth=2.0)

for i in range(4,150,5):
	plt.axvline(i+0.5, color='k', linewidth=1.0, linestyle='--')

plt.ylabel('Device')
plt.yticks(range(len(dimensions)), dimensions)
for i in range(0, len(dimensions), 3):
	plt.axhline(i-.5, color='k', linewidth=2.0)
plt.show()
'''



