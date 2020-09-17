#############################
## Model for TILE38_Control	 
## TILE_38 Model
#############################

################
## Requirements
###############
import json
import os.path
################
#########################
## Creates the REST API CONFIG JSON FILE
#########################

TILE38_CONFIG_FILE_NAME = "TILE38_Config.json"
CONFIG_FILE_LOCATION = "../config/"
TOTAL_TILE38_FILE_CONFIG_PATH = CONFIG_FILE_LOCATION + TILE38_CONFIG_FILE_NAME

def createConfigFile():
	settingsTemplate = {"TILE38_DOWNLOAD_URL": "",  "TILE38_ENDPOINT_URL": "", "TILE38_PID": "" }
	if(os.path.isfile(TOTAL_TILE38_FILE_CONFIG_PATH)):
		return True
	else:
		with open(TOTAL_TILE38_FILE_CONFIG_PATH, 'w') as jsonConfig:
    			json.dump(settingsTemplate, jsonConfig, sort_keys=True, indent=4)
		return False
#########################	
## Returns REST API USERNAME
########################
def getConfigFileData(Field):
	if(os.path.isfile(TOTAL_TILE38_FILE_CONFIG_PATH)):
		with open(TOTAL_TILE38_FILE_CONFIG_PATH, "r") as jsonCONFIG:
    			configData = json.load(jsonCONFIG)
			return (configData[Field])
	else:
		print("REST API CONFIG NOT FOUND")
		return False
##########################
## Sets REST API CONFIG VALUES
#########################

def setConfigFileData(Field, Value):
	with open(TOTAL_TILE38_FILE_CONFIG_PATH, "r") as jsonFile:
    		data = json.load(jsonFile)
	data[Field] = Value
	with open(TOTAL_TILE38_FILE_CONFIG_PATH, "w") as jsonFile:
    		json.dump(data, jsonFile, sort_keys=True, indent=4)

###########################
##  Returns True/False if Config file exists
##############################
def doesConfigFileExist():
	if(os.path.isfile(TOTAL_TILE38_FILE_CONFIG_PATH)):
                return True
        else:
                return False
	
