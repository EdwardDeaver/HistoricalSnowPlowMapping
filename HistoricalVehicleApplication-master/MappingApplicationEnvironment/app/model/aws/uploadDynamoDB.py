import time
import uuid
import boto3
import json
from decimal import *
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
dynamodb_client = boto3.client('dynamodb')
def createStreetDataTable(tableName):
        existing_tables = dynamodb_client.list_tables()['TableNames']

        if(tableName not in existing_tables):
                table = dynamodb.create_table(
                TableName=tableName,
                KeySchema=[
                {
                        'AttributeName': 'Street_ID',
                        'KeyType': 'HASH'  #Sort key
                }
                
		],
                AttributeDefinitions=[
                {
                        'AttributeName': 'Street_ID',
                        'AttributeType': 'N'
                }
                ],

                ProvisionedThroughput={
                        'ReadCapacityUnits': 11,
                        'WriteCapacityUnits': 11,
                }
        )
                return True
        else:
                return False

def createHistoricalTable(tableName):
	existing_tables = dynamodb_client.list_tables()['TableNames']
 
	if(tableName not in existing_tables):
		table = dynamodb.create_table(
		TableName=tableName,
		KeySchema=[
           	{
            		'AttributeName': 'vehicle_id',
           		'KeyType': 'HASH'  #Sort key
        	},
 		{
                        'AttributeName': 'messageUploadTime',
                        'KeyType': 'RANGE'  #Partition key
                }

		],
		AttributeDefinitions=[
		{
			'AttributeName': 'messageUploadTime',
			'AttributeType': 'N'
		},

                {
                        'AttributeName': 'vehicle_id',
                        'AttributeType': 'N'
                }
		],
		
		ProvisionedThroughput={
        		'ReadCapacityUnits': 10,
        		'WriteCapacityUnits': 10,
        	}
	)
		return True
	else:
		return False
############################
## Issues that dynamo cant support floats
## So now split the number into whole and decimals 
## https://stackoverflow.com/questions/28425117/dynamodbnumbererror-on-trying-to-insert-floating-point-number-using-python-boto
## https://docs.python.org/3/library/decimal.html
#dataToSend ={"@type": "PagedGpsMessageResult", "index": 0, "limit": 100, "count": 100, "total": 113, "gpsMessage": [{"messageTime": "2018-09-28T14:43:29Z", "satellite":False , "latitude": 43.055644, "longitude": -76.107591, "accuracy": {"@units": "MILES", "value": 0.006213711922373339}, "odometer": {"@units": "MILES", "@timestamp": "2018-09-28T14:43:29Z", "value": 1773.7}, "keyOn": False, "parked": False, "lastSpeed": 0, "avgSpeed": 0, "maxSpeed": 5, "vehicleId": 951175}]}
def batchVehicleIDUploadToDynamoDB(tableName, data):
	existing_tables = dynamodb_client.list_tables()['TableNames']
	print(existing_tables)
	#table = dynamodb.Table(tableName)

	#numberCount = table.item_count
	#print(numberCount)
	if(tableName in existing_tables):
		table = dynamodb.Table(tableName)
		numberCount = table.item_count
		print(numberCount)
		numberCount = numberCount +1	

		data = json.dumps(data)
		data = json.loads(data)
		currentSentTime = time.time()
		print(data)
		try:
			with table.batch_writer() as batch:
				counter = 1
				for i in data["gpsMessage"]:
							
					batch.put_item(
           	 			Item={
						'vehicle_id':i["vehicleId"],
						'messageTime': i["messageTime"],
						'messageUploadTime':  Decimal(str(currentSentTime)),
						'latitude': Decimal(str(i["latitude"])),
						'longitude':  Decimal(str(i["longitude"]))	
	            			})
					counter = counter +1
					time.sleep(0.5)
			return True
		except Exception as error:
			return repr(error)
		return True
	else:
		return False

############################
## Issues that dynamo cant support floats
## So now split the number into whole and decimals
## https://stackoverflow.com/questions/28425117/dynamodbnumbererror-on-trying-to-insert-floating-point-number-using-python-boto
## https://docs.python.org/3/library/decimal.html
#dataToSend ={"@type": "PagedGpsMessageResult", "index": 0, "limit": 100, "count": 100, "total": 113, "gpsMessage": [{"messageTime": "2018-09-28T14:43:29Z", "satellite":False , "latitude": 43.055644, "longitude": -76.107591, "accuracy": {"@units": "MILES", "value": 0.006213711922373339}, "odometer": {"@units": "MILES", "@timestamp": "2018-09-28T14:43:29Z", "value": 1773.7}, "keyOn": False, "parked": False, "lastSpeed": 0, "avgSpeed": 0, "maxSpeed": 5, "vehicleId": 951175}]}
def batchStreetIDUploadToDynamoDB(tableName, data):
	existing_tables = dynamodb_client.list_tables()['TableNames']
	print(existing_tables)
        #table = dynamodb.Table(tableName)

        #numberCount = table.item_count
        #print(numberCount)
	if(tableName in existing_tables):
		table = dynamodb.Table(tableName)
		numberCount = table.item_count
		print(numberCount)
		numberCount = numberCount +1
		data = json.dumps(data)
		data = json.loads(data)
		currentSentTime = time.time()
		print(data)
		try:
			with table.batch_writer() as batch:
				counter = 1
				for i in data["features"]:
					if("I 690" in i["properties"]["FULLNAME"]):
						print("none")
					elif("I 81" in i["properties"]["FULLNAME"]):
						print("non")
					elif("I 481" in i["properties"]["FULLNAME"]):
                        			print("jsjsjsjsj")
					else:
						#print(i["properties"]["FULLNAME"])
						#print(i["properties"]["CITYST_ID"])
						batch.put_item(
                                        	Item={
                                                	'Street_ID':i["properties"]["CITYST_ID"],
							'StreetName': i["properties"]["FULLNAME"],                                          
        						'Activity': "PLOW",
							'Color': "Red",
							'Time': Decimal(str(currentSentTime))           	
	})
				time.sleep(0.5)
			return True
		except Exception as error:
			return repr(error)
		return True
	else:
		return False

