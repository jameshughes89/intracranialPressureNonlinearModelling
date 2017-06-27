'''
Counts the number of times each variable was in all of the generated models. 
'''

import numpy as np
import csv
import sys
import matplotlib.pylab as plt

subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']


dimensions=['PLETH', 'ECG-V', 'ABP', 'ICP']

allBestVal = []
allBestInd = []
allmsE = []
allabE = []

allVarCounts = []

for tme in times:
	allBestVal = []
	allBestInd = []
	allmsE = []
	allabE = []

	allVarCounts = []
	for sub in subjects:
		print sub, tme
		fcount = np.zeros(len(dimensions))
		for i in range(50):
			iFile = csv.reader(open('../jGPv9-ICP/src/outs/' + str(sub) + '-' + tme + '_lessFeatures/' + str(i) + '_multi.txt','r'), delimiter='\t')
			fBool = [False] * 4		
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
	plt.matshow(allVarCounts, aspect='auto')
	plt.colorbar(label='% Models Containing Feature')
	plt.title('Features When Trained on ' + tme + ' of the Data')
	plt.ylabel('Subjects')

	plt.yticks(range(len(subjects)), subjects, rotation=0)
	#for i in range(len(tasks)):
	#	plt.axhline(i*len(subjects)*len(takes)-1, color='k', linewidth=2.0)

	#for i in range(4,150,5):
	#	plt.axhline(i, color='k', linewidth=1.0, linestyle='--')


	plt.xlabel('Device')
	plt.xticks(range(len(dimensions)), dimensions,rotation=90)
	for i in range(0, len(dimensions), 3):
		plt.axvline(i-.5, color='k', linewidth=2.0)
	#plt.show()

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



