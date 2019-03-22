import os
path = os.getcwd() #get the current path
string_pos = path.index('Python') #find the python folder
base_path = path[:string_pos]+'Python\\' #create a base filepath string

import git

def refresh_report(folder_dir):

	print("Refreshing repo for: "+folder_dir)

	try:
		repo = git.Repo(folder_dir)
		o = repo.remotes.origin
		o.pull()
		print("REFRESH COMPLETE!")
	except:
		print("REFRESH REPORT FAILED FOR: "+folder_dir)


refresh_report(base_path+'Email-Reader')
refresh_report(base_path+'Web-Service-Reader')
refresh_report(base_path+'Functions')