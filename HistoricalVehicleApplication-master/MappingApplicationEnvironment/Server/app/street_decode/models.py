#############################
## Model For KML decode
#############################

################
## Requirements

import json
import os
import requests


################
#########################
## Checks if file exists in data/streets/
#########################
defaultLocation = "../data/streets/"
myStreetJSON= "street_cord.json"


def createJSON():
	settingsTemplate = {"JSON_STREETS_URL": ""}
	if(os.path.isfile("../static/street_cord_json_config.json")):
		return True
	else:
		with open('../static/street_cord_json_config.json', 'w') as jsonConfig:
    			json.dump(settingsTemplate, jsonConfig, sort_keys=True, indent=4)
		return False

def downloadJSON(fileURL, fileName, fileLocation):
	url = fileURL
	data = requests.get(fileURL)
	data = data.json()
	try:
		with open(fileLocation+fileName, 'w') as jsonConfig:
                        json.dump(data, jsonConfig, sort_keys=False, indent=4)
			print("SUCCESS")
			return True
	except:
		return False


def getJSON(fileName, fileLocation):
        try:
                with open(fileLocation+fileName) as jsonConfig:
                        myJSON = json.load(jsonConfig)
                
                        return myJSON
        except:
                return False

def exportJSON(data, fileName, fileLocation):
	try:
        	with open(fileLocation+fileName, 'w') as jsonConfig:
                	json.dump(data, jsonConfig, sort_keys=False, indent=4)
                        print("SUCCESS")
                        return True
        except:
                return False



