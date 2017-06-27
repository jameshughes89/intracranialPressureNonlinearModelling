'''
Generates linear models with OLS

First bit does all features
Second bit does the subset of features

'''
import csv
import numpy as np
import sys
import statsmodels.api as sm

subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
times = ['all','250','1s']


# This bit does all features
for tme in times:
	# sets up the file where we will put the expressions
	# each file will be of the time group (so 30 in each of the 3 files for the 3 times)
	oFile = open('./bestLinearExpressions_' + str(tme) + '.py','w')
	oFile.write("from math import *\n\n")
	fs='funcs = ['
	
	# go through each subject for the current time
	for count, sub in enumerate(subjects):
		print sub, tme
		data = np.array(list(csv.reader(open('../PNdata/' + str(sub) + '-' + str(tme) + '.csv', 'r')))).astype(np.float)	# load the data (it's ugly, i know)

		y = data[:,-1]									# last col is what we regress to (y)
		X = data[:,:-1]									# all other cols are the data points (regressors)
		
		X = sm.add_constant(X)							# adds a constant for error: e (y = BX + e)
		results = sm.OLS(y,X).fit()						# does the actual regression 
		B = results.params								# get those Betaz bro
		
		eqn = str(B[0]) + ' * 1 + '						# Doing it this way because error goes first (error beta value on constant added up there)
		for i in range(1, len(B)):
			eqn = eqn + str(B[i]) + ' * v' + str(i-1)	# minus 1 because i starts at 1
			if i != len(B)-1:			
				eqn = eqn + ' + '						# add addition if it's NOT the last beta value

		oFile.write('def func_' + str(count) + '(v0,v1,v2,v3,v4,v5,v6): return ' + eqn + '\n')

		fs = fs + 'func_' + str(count)
		if count != len(subjects) - 1:					# don't acutally need this; you can have a trailing comma
			fs = fs + ','	

	fs = fs + ']'
	oFile.write("\n" + fs)

	oFile.write("\n\ndef getFuncs(): return funcs\n")
	oFile.close()







# This bit does subset of features (copy paste because lazy)
for tme in times:
	# sets up the file where we will put the expressions
	# each file will be of the time group (so 30 in each of the 3 files for the 3 times)
	oFile = open('./bestLinearExpressions_' + str(tme) + '_lessFeatures.py','w')
	oFile.write("from math import *\n\n")
	fs='funcs = ['
	
	# go through each subject for the current time
	for count, sub in enumerate(subjects):
		print sub, tme
		data = np.array(list(csv.reader(open('../PNdata/' + str(sub) + '-' + str(tme) + '_lessFeatures.csv', 'r')))).astype(np.float)	# load the data (it's ugly, i know)

		y = data[:,-1]					# last col is what we regress to (y)
		X = data[:,:-1]					# all other cols are the data points (regressors)
		
		X = sm.add_constant(X)			# adds a constant for error: e (y = BX + e)
		results = sm.OLS(y,X).fit()		# does the actual regression 
		B = results.params					# get those Betaz bro
		
		eqn = str(B[0]) + ' * 1 + '		# Doing it this way because error goes first (error beta value on constant added up there)
		for i in range(1, len(B)):
			eqn = eqn + str(B[i]) + ' * v' + str(i-1)	# minus 1 because i starts at 1
			if i != len(B)-1:			
				eqn = eqn + ' + '		# add addition if it's NOT the last beta value

		oFile.write('def func_' + str(count) + '(v0,v1,v2,v3): return ' + eqn + '\n')

		fs = fs + 'func_' + str(count)
		if count != len(subjects) - 1:			# don't acutally need this; you can have a trailing comma
			fs = fs + ','	

	fs = fs + ']'
	oFile.write("\n" + fs)

	oFile.write("\n\ndef getFuncs(): return funcs\n")
	oFile.close()
