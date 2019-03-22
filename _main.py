import os
path = os.getcwd() #get the current path
string_pos = path.index('Python') #find the python folder
base_path = path[:string_pos]+'Python\\' #create a base filepath string

import datetime
import git
errors = 0

def refresh_report(folder_dir):

	print("Refreshing repo for: "+folder_dir)
	errors = 0

	try:
		repo = git.Repo(folder_dir)
		o = repo.remotes.origin
		o.pull()
		print("REFRESH COMPLETE!")
		print("")
	except:
		errors += 1
		print("REFRESH REPORT FAILED FOR: "+folder_dir)
		print("")

	return errors

print('########################################')
print("RUNNING GIT REFRESH PROCESS")
print('########################################')

start_time = datetime.datetime.now() #need for process time printing

errors += refresh_report(base_path+'Email-Reader')
errors += refresh_report(base_path+'Web-Service-Reader')
errors += refresh_report(base_path+'Functions')
errors += refresh_report(base_path+'Service-Report')

finish_time = datetime.datetime.now()

print('')
print('########################################')
print("PROCESS COMPLETE")
print("Number of Errors: "+str(errors))
print('Start: '+str(start_time))
print('End: '+str(finish_time))
print('Time Taken: '+str(finish_time - start_time))
print('########################################')

#TESTS TO SEE IF THE SCHEDULER IS WORKING
#file1 = open("test.txt","w")
#file1.close()