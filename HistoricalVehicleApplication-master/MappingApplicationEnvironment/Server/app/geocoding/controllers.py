########################
## Controller made to control REST OPERATIONs
########################
######################
## Made by: Edward C. Deaver, IV
####################
from itertools import cycle
import view 
import models
import requests
import json

#####################################################
## Set's up json doc with information
#####################################################
def setupAPIConfig():
	print("This setup will configure the geocoding_rest_api.json file located in: app/static/ \n")

	COUNTRY_ORIGIN = view.getUserInput("What country is this being setup in? Ex. USA[United States], CA[Canada], MX[Mexico]\n>")
	models.setGeoCodeAPIData("COUNTRY_ORIGIN", COUNTRY_ORIGIN)

	STATE_ORIGIN = view.getUserInput("What state is this being setup for? Ex. California, Wisconson, New York\n>")
	models.setGeoCodeAPIData("STATE_ORIGIN", STATE_ORIGIN)

	CITY_ORIGIN = view.getUserInput("What city is this being setup for? Ex. Los Angels, Madison, Syracuse\n>")
	models.setGeoCodeAPIData("CITY_ORIGIN", CITY_ORIGIN)

	REST_END_POINT = view.getUserInput("What is your REST API Endpoint? Ex. 'https://www.mapquestapi.com/'\n>")
	models.setGeoCodeAPIData("REST_API_ENDPOINT", REST_END_POINT)
	
	REST_API_KEY = view.getUserInput("What is your REST GEOCODE API KEY?\n>")
	REST_API_KEY = REST_API_KEY.split(",")
	models.setGeoCodeAPIData("REST_API_KEY", REST_API_KEY)
	
	REST_API_SECRET = view.getUserInput("What is your REST GEOCODE API SECRET?\n>")
	models.setGeoCodeAPIData("REST_API_SECRET", REST_API_SECRET)
###########################################################################################################
## Get's rest GeoCoded data from Mapquest
## Returns JSON of return messsage or status code
###########################################################################################################
def getRESTData(REST_ENDPOINT_URL, REST_ENDPOINT_SERVICE, REST_API_KEY, STREET_ADDRESS, CITY, STATE, COUNTRY):
	

	url = REST_ENDPOINT_URL + REST_ENDPOINT_SERVICE
	address = STREET_ADDRESS+", "+CITY+", "+STATE+", "+COUNTRY
	print(address)
	querystring = {"key":REST_API_KEY,"outFormat":"json","maxResults":"1","location":address}

	headers = {
    		'Cache-Control': "no-cache",
    		}

	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)
	return (response)
####################################
## geoCode's address
## Returns lat lon in Array format
## It will loop till it finds a usable key
#####################################
def geoCode(Address):
	pool_of_keys = cycle(models.getGeoCodeAPIData("REST_API_KEY"))
	print(pool_of_keys)
	key = next(pool_of_keys)
	response = getRESTData(models.getGeoCodeAPIData("REST_API_ENDPOINT"), "geocoding/v1/address",key, Address, "Syracuse", "New York", "USA" )
	print("STATUS CODE")
	print(response.status_code)
	holdKey = key
	while(response.status_code  == 403):
	        key = next(pool_of_keys)
		print(key)
		response = getRESTData(models.getGeoCodeAPIData("REST_API_ENDPOINT"), "geocoding/v1/address", key, Address, models.getGeoCodeAPIData("CITY_ORIGIN"), models.getGeoCodeAPIData("STATE_ORIGIN"), models.getGeoCodeAPIData("COUNTRY_ORIGIN") )
		if (key == holdKey):
		
			raise ValueError('stuff is not in content')

	response = response.json()
	latlong = [response["results"][0]["locations"][0]["displayLatLng"]["lat"],response["results"][0]["locations"][0]["displayLatLng"]["lng"] ]

	return latlong	




######################################
## Creates the setup for the geocode API
######################################
def setup():
	
	Exists = models.createGeoCodeAPIConfigFile()
	if(not Exists):
		setupAPIConfig()











