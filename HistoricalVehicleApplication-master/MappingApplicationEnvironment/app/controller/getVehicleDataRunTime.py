import sys
sys.path.append('../')
#import json
import boto3
from model import dataManage
from model import vehicleManage
import time
from decimal import *

startTime = None
restartTime = None
incrementTime = 600
def main():
	#response = dataManage.createTables("HistoricalVehicleRecord")
	#responseStreets = dataManage.createTables("StreetData")
	#print(response)
	#if(response == True):
	getVehicleDataRuntime()
def getVehicleDataRuntime():
	validate()
	starttime = time.time()
	print(starttime)
	
	while(True):
		
		outData = getVehicleLocation()
		#print(outData)
		if(type(outData) == str):
			if(len(outData) == 3):
				getVehicleDataRuntime()
		dataManage.saveDataJSONFile(outData, "vehicleLocations")
		'''
		if(type(outData) == int):
			while(outData == 401 or outData == 403):
				refreshAPIKey()
				outData = getVehicleLocation()
				dataManage.saveDataJSONFile(outData, "vehicleLocations")
		'''
		#uploadToS3(startTime)
		#time.sleep(60)
		dataManage.uploadToDynamo("HistoricalVehicleRecord", outData)
		if((time.time() - starttime)>incrementTime):
			#dataManage.uploadToS3('vehicleLocations.json', '../data/', "",'mappingapplicationtestbucket'
			s3 = boto3.resource('s3')
			s3.meta.client.upload_file('../../data/vehicleLocations.json', 'mappingapplicationtestbucket', 'vehicleLocations.json')
			starttime = time.time()

 	
def getVehicleLocation():
	restAPIKey = dataManage.getConfigData("verizonFleetConfig", "REST_API_KEY", False)
	print(restAPIKey)
	apiKeyType = dataManage.getConfigData("verizonFleetConfig", "REST_API_KEY_TYPE", False)
	groupName  = dataManage.getConfigData("verizonFleetConfig", "REST_VEHICLE_GROUP", False)
	response   = vehicleManage.getVehicleLocations(str(groupName), restAPIKey, apiKeyType)
	return response
def validate():
	username  = dataManage.getConfigData("verizonFleetConfig", "REST_API_USERNAME", False)
	password  = dataManage.getConfigData("verizonFleetConfig", "REST_API_PASSWORD", False)
	response  = vehicleManage.validateAPI(username, password)
	dataManage.updateConfigData("verizonFleetConfig", "REST_API_KEY", response['access_token'])
	dataManage.updateConfigData("verizonFleetConfig", "REST_API_KEY_REFRESH", response['refresh_token'])
	return response
'''def refreshAPIKey():
	username  = dataManage.getConfigData("verizonFleetConfig", "REST_API_USERNAME", False)
	password  = dataManage.getConfigData("verizonFleetConfig", "REST_API_PASSWORD", False)
	refreshKey = dataManage.getConfigData("verizonFleetConfig", "REST_API_KEY_REFRESH", False)
	response = vehicleManage.refreshToken(refreshKey, username, password)
	return response
'''
#getVehicleDataRuntime()
main()

