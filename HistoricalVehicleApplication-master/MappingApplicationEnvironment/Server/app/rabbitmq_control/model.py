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

CONFIG_FILE_NAME = "RABBITMQ_Config.json"
CONFIG_FILE_LOCATION = "../config/"
TOTAL_FILE_CONFIG_PATH = CONFIG_FILE_LOCATION + CONFIG_FILE_NAME

def createConfigFile():
	settingsTemplate = { "RABBITMQ_ENDPOINT_URL": "", "RABBITMQ_USER": "", "RABBITMQ_PID": "" }
	if(os.path.isfile(TOTAL_FILE_CONFIG_PATH)):
		return True
	else:
		with open(TOTAL_FILE_CONFIG_PATH, 'w') as jsonConfig:
    			json.dump(settingsTemplate, jsonConfig, sort_keys=True, indent=4)
		return False
#########################	
## Returns REST API USERNAME
########################
def getConfigFileData(Field):
	if(os.path.isfile(TOTAL_FILE_CONFIG_PATH)):
		with open(TOTAL_FILE_CONFIG_PATH, "r") as jsonCONFIG:
    			configData = json.load(jsonCONFIG)
			return (configData[Field])
	else:
		print("REST API CONFIG NOT FOUND")
		return False
##########################
## Sets REST API CONFIG VALUES
#########################

def setConfigFileData(Field, Value):
	with open(TOTAL_FILE_CONFIG_PATH, "r") as jsonFile:
    		data = json.load(jsonFile)
	data[Field] = Value
	with open(TOTAL_FILE_CONFIG_PATH, "w") as jsonFile:
    		json.dump(data, jsonFile, sort_keys=True, indent=4)

###########################
##  Returns True/False if Config file exists
##############################
def doesConfigFileExist():
	if(os.path.isfile(TOTAL_FILE_CONFIG_PATH)):
                return True
        else:
                return False
	
