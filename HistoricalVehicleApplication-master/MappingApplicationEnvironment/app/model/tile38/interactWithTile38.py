import redis
import json
import subprocess

#LOCATION_OF_TILE38 = "../../../dependency/TILE38/tile38-1.13.0-linux-amd64/"
#TILE38_PID = False
#Description: connect to Tile38 
#Pre: Tile38 Server is running 
#     URL is valid [3 digit, 3 digit, 3 digit, 3 digit] 
#     URL must be string type
#Post: returns Redis object of the connected object if the server is up.
#      If the function can not connect to the Tile38 function willl return false
def connectToTile38(URL):
	try:
		client = redis.Redis(host="0.0.0.0", port=9851)
		client.ping()	

	except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
		return None
	else:
		return client

#Description: This method creates a hook for the specified geoCord set
#Pre: Tile 38 server is running
#	tile38ClientOBJ is a valid object 
#	hookPointURL is a valid AMQP url for RabbitMQ
#	endHookPointName is the CITYST_ID of the geocords being used
# 	fenceCordsArray is the array of geocords [[]]
#Post:
#	Return true for success
# 	Return false for failure
def loadGeoFences(tile38ClientOBJ, hookPointURL, endHookPointName, fenceCordsArray):
	dictionaryOfPolygon = {"type": "Polygon", "coordinates": fenceCordsArray}
	jsonDropOfPolygon = json.dumps(dictionaryOfPolygon)
	
	try:
		debug = tile38ClientOBJ.execute_command('SETHOOK', endHookPointName,hookPointURL, 'WITHIN', 'fleet', 'DETECT', 'inside', 'object', jsonDropOfPolygon)
	
	except(redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
		return None
	else:
		return debug

#Description: This method sets the truck location
#Pre:
#	 Tile 38 server is running
#	tile38ClientOBJ is a valid object
#	truckName valid string, value is the vehicle ID
# 	Latitude is a valid -82 to 80 . This is the one that goes up and down the globe
# 	Longitude valid -180 to + 180. This is the one that goes horizontally around the earth. 
#Post:
#	Fleet turckobject location set
#	If Debug runs into issues returns false
#	else: None
def setFleetLocation(tile38ClientOBJ, truckName, latitude,longitude):
	try:
		debug = tile38ClientOBJ.execute_command('SET', 'FLEET', truckName,"POINT",latitude,longitude)
	except(redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
		return None
	else:
		return debug


def startTile38():
	try:
		debug = subprocess.Popen(['nohup', './'+LOCATION_OF_TILE38+'/tile38-server','-q', '&'])
	except(redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
		return None
	else:
		return debug
	#print(debug)
	#TILE38_PID = debug.pid
	
	#print(TILE38_PID)
	#try:
	#global TILE38_PID
	#if(TILE38_PID is True):
#		print("process exists")
#	else:
#		debug = subprocess.Popen(['nohup', './'+locationOfTile38Binary+'/tile38-server','-q', '&'])
#		TILE38_PID = True
#		print(TILE38_PID)
#		return debug
	#https://stackoverflow.com/questions/31039972/python-subprocess-popen-pid-return-the-pid-of-the-parent-script/31040013
	#	
	#except:
	#	return False
	#else:
	#	return debug
		
	
