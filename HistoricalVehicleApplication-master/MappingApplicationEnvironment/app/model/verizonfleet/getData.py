## Command to get vehicle locations
## This is meant to be a public facing method so you can just get the reponse of vehicles
## Using Flag: KeyOn == True this means the vehicle is ON
## Returns [] with {} inside
############################################
import json
import requests
from requests.auth import HTTPBasicAuth

def queryAPI(requestType,apiEndPoint,modifier, apiKey, apiKeyType, payload, username, password):
	repsonse = ""
	url = apiEndPoint+modifier
	print(url)
	print(apiKey)
	if(requestType=="GET"):
		headers = {'Authorization': "Bearer "+apiKey,'Accept': "application/vnd.networkfleet.api-v1+json",'Content-Type': "application/vnd.networkfleet.api-v1+json",'Cache-Control': "no-cache"}
		response = requests.request("GET", url, headers=headers)
		print(type(response.status_code))
		if(response.status_code != 200):
			return str(response.status_code)
		else:
			return response.json()
		#response.raise_for_status()
	if(requestType=="POST"):
		headers = {'Content-Type': "application/x-www-form-urlencoded"}
		response = requests.request("POST", url, data=payload, headers=headers,  auth=(username, password))
		if(response.status_code != 200):
			return str(response.status_code)
		else:
			return response.json()
#print(refreshToken("ab1275cf-f1db-42de-a579-89c6e21495ba", "Edeaver", "6e691d92eec0a4dcc821370ec0a9a52f"))


#print(getVehicleLocations(False, "https://api.networkfleet.com/", "415282", "4060b6c8-7cd3-40be-ba78-13e9492fdf15", "Bearer"))


