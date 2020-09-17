from .jsonmanage import jsonCreate
from .jsonmanage import jsonRead
from .aws import uploadS3
from .aws import uploadDynamoDB

def saveConfigJSONFile(data, filename):
	#print("MODEL HIT")
	jsonCreate.createJSONFile(data, "../../config/", filename)

def saveDataJSONFile(data, filename):
        #print("MODEL HIT")
        jsonCreate.createJSONFile(data, "../../data/", filename)
##############
## Purpose to return data from a config file
## filename -- fileName of config data
## fieldname -- fieldName in config file
## full -- T/F Full file or specific
## Return data -- no defined type.
##################################

def getData(filename, fieldname, full):
        data =  jsonRead.readJSONFile(filename, "../../data/")
        if(full):
                return data
        else:
                return data[fieldname]



##############
## Purpose to return data from a config file
## filename -- fileName of config data
## fieldname -- fieldName in config file
## full -- T/F Full file or specific
## Return data -- no defined type. 
##################################

def getConfigData(filename, fieldname, full):
	data =	jsonRead.readJSONFile(filename, "../../config/")
	if(full):
		return data
	else:
		return data[fieldname]

##################
## Purpose to update a config file
## filename -- filename to be updated
## fieldname -- is the field name in the config data to be updated
## newData -- is the new field data
###################
def updateConfigData(filename, fieldname, newData):
	fileData = getConfigData(filename, "", True)
	#print(fileData)
	fileData[fieldname] = newData
	#print("/n\n\n")
	#print(fileData)
	saveConfigJSONFile(fileData, filename)


#########################
### Purpose to upload file to s3 
## filename -- file to upload to s3
## fileLocation -- file to upload to s3
## serverLocation -- file location path on server
############################

def uploadToS3(filename, FileLocation, serverFilePath, bucketName):
	try:
		uploadS3.uploadToS3Bucket(filename, bucketName, serverFilePath+filename) 
	except:
		return False
		
'''
print(getConfigData("verizonFleetConfig", "REST_API_AUTH_ENDPOINT", False))
print(updateConfigData("verizonFleetConfig", "REST_API_AUTH_ENDPOINT", "THISISCRAZY"))
print(getConfigData("verizonFleetConfig", "REST_API_AUTH_ENDPOINT", False))
'''

def createTables(tableName):
	if(tableName == "HistoricalVehicleRecord"):
		response =  uploadDynamoDB.createHistoricalTable("HistoricalVehicleRecord")
	if(tableName == "StreetData"):
		response =  uploadDynamoDB.createStreetDataTable("StreetData")
	return response

def uploadToDynamo(tablename, data):
	if(tablename == "HistoricalVehicleRecord"):
		uploadDynamoDB.batchVehicleIDUploadToDynamoDB(tablename, data)
	if(tablename == "StreetData"):
		uploadDynamoDB.batchStreetIDUploadToDynamoDB(tablename, data)
