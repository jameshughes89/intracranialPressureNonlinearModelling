################################################
subjects = [3029993, 3033031, 3083337, 3094054, 3096171, 3105502, 3169632, 3262086, 3269261, 3289177, 3367596, 3379471, 3460047, 3463681, 3505904, 3516004, 3555523, 3562822, 3582988, 3599360, 3600995, 3607634, 3623238, 3645431, 3646209, 3662063, 3721988, 3738640, 3779174, 3781713]
takes = ['all', '250', '1s']

################################################

for s in range(0,1):
    for tke in takes:
		oFile = open(tke + '.sh','w')
		for sub in subjects:
			for i in range(0, 50, 1):
				#MIND THE TASK AND L VALUE HERE!!!!
				oFile.write('echo ' + str(sub) + '-' + tke + ' ' +str(i)+ ' 1 ' + str(s) +'\n')
				oFile.write('java Centre ' + str(sub) + '-' + tke + ' ' +str(i)+ ' 1 ' + str(s) +'\n')
		oFile.close()



# reverse bit --- to run on other comp

################################################
subjects.reverse()
takes = ['all']
################################################

for s in range(0,1):
    for tke in takes:
		oFile = open(tke + '-REV.sh','w')
		for sub in subjects:
			for i in range(0, 50, 1):
				#MIND THE TASK AND L VALUE HERE!!!!
				oFile.write('echo ' + str(sub) + '-' + tke + ' ' +str(i)+ ' 1 ' + str(s) +'\n')
				oFile.write('java Centre ' + str(sub) + '-' + tke + ' ' +str(i)+ ' 1 ' + str(s) +'\n')
		oFile.close()

