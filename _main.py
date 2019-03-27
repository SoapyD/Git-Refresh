import os
path = os.getcwd() #get the current path
string_pos = path.index('Python') #find the python folder
base_path = path[:string_pos]+'Python\\' #create a base filepath string

func_dir = base_path+"functions\\"
exec(open(func_dir+"functions.py").read()) #file contains all sql reading and db interaction scripts

import datetime
import git
errors = 0

def refresh_report(folder_dir):

	u_print("Refreshing repo for: "+folder_dir)
	errors = 0

	try:
		repo = git.Repo(folder_dir)
		o = repo.remotes.origin
		o.pull()
		u_print("REFRESH COMPLETE!")
		u_print("")
	except:
		errors += 1
		u_print("REFRESH REPORT FAILED FOR: "+folder_dir)
		u_print("")

	return errors

u_print('########################################')
u_print("RUNNING GIT REFRESH PROCESS")
u_print('########################################')

start_time = datetime.datetime.now() #need for process time u_printing

errors += refresh_report(base_path+'Email-Reader')
errors += refresh_report(base_path+'Web-Service-Reader')
errors += refresh_report(base_path+'Functions')
errors += refresh_report(base_path+'Service-Report')

finish_time = datetime.datetime.now()

u_print('')
u_print('########################################')
u_print("PROCESS COMPLETE")
u_print("Number of Errors: "+str(errors))
u_print('Start: '+str(start_time))
u_print('End: '+str(finish_time))
u_print('Time Taken: '+str(finish_time - start_time))
u_print('########################################')

save_process(start_time, finish_time, str(finish_time - start_time), "Git-Refresh")

#TESTS TO SEE IF THE SCHEDULER IS WORKING
#file1 = open("test.txt","w")
#file1.close()