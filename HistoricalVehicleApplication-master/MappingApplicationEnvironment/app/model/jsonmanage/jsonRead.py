import json

import os

##########
## Purpose: To return a json file
## fileName -- File name of file requested
## fileLocation -- filelocation
## Return: json file data
##################################

def readJSONFile(fileName, fileLocation):
	try:
		with open(fileLocation+fileName+".json", 'r') as openFile:
    			fileData = json.load(openFile)
	except:
		print(os.path.dirname(os.path.abspath(__file__)))
		files = os.listdir(fileLocation)
		for name in files:
    			print(name)
		return False
	else:
		return fileData
	
