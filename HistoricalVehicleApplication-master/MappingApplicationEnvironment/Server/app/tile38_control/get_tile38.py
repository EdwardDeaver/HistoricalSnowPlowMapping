###############################################
## Downloads Tile 38			#######
## Written by: Edward C. Deaver, IV     #######
###############################################
###############################################
## IMPORTS				#######
###############################################
import requests
import os
import tarfile
DEPENDENCIES_FILE_NAME = "../dependencies/"
local_filename = ""

def download_file(url):
	local_filename = url.split('/')[-1]
    	# NOTE the stream=True parameter
    	r = requests.get(url, stream=True)
    	print("Downloading "+ local_filename)
	with open(DEPENDENCIES_FILE_NAME+local_filename, 'wb') as f:
        	for chunk in r.iter_content(chunk_size=1024): 
	
           		if chunk: # filter out keep-alive new chunks
                		f.write(chunk)
                		#f.flush() commented by recommendation from J.F.Sebastian
    	unzipFile(local_filename, DEPENDENCIES_FILE_NAME)
	fileCleanup(local_filename, DEPENDENCIES_FILE_NAME)
    	return local_filename

def unzipFile(filename, filepath):
	with tarfile.open(filepath+filename) as tar:
    		tar.extractall(path=filepath)
	return True

def fileCleanup(filename, filepath):
	if os.path.exists(filepath+filename):
  		os.remove(filepath+filename)
		return True
	else:
  		print("The file does not exist")
		return False



