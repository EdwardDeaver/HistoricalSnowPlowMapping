#############################
## Model For REST API Call
## MAPQUEST 
#############################

################
## Requirements

import json
import os.path
################
#########################
## Creates the REST API CONFIG JSON FILE
#########################

def createGeoCodeAPIConfigFile():
	settingsTemplate = {"REST_API_ENDPOINT": "", "REST_API_KEY": [], "REST_API_SECRET": "", "CITY_ORIGIN": "", "STATE_ORIGIN": "", "COUNTRY_ORIGIN": ""}
	if(os.path.isfile("../static/geocoding_rest_api.json")):
		return True
	else:
		with open('../static/geocoding_rest_api.json', 'w') as jsonConfig:
    			json.dump(settingsTemplate, jsonConfig, sort_keys=True, indent=4)
		return False
#########################	
## Returns REST API USERNAME
########################
def getGeoCodeAPIData(Field):
	if(os.path.isfile("../static/geocoding_rest_api.json")):
		with open('../static/geocoding_rest_api.json', "r") as jsonCONFIG:
    			configData = json.load(jsonCONFIG)
			
			
			return (configData[Field])
	else:
		print("REST API CONFIG NOT FOUND")
		return False
##########################
## Sets REST API CONFIG VALUES
#########################

def setGeoCodeAPIData(Field, Value):
	with open("../static/geocoding_rest_api.json", "r") as jsonFile:
    		data = json.load(jsonFile)

	
	data[Field] = Value

	with open("../static/geocoding_rest_api.json", "w") as jsonFile:
    		json.dump(data, jsonFile, sort_keys=True, indent=4)


