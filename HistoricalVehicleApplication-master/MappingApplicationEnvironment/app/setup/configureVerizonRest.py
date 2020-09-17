########################
## Setup Verizon REST API
########################
######################
## Made by: Edward C. Deaver, IV
####################
### External Imports
import getpass
import pprint
import reques



import sys
sys.path.append('../')

from view  import terminalDisplay as display

from model import dataManage


def setup():
        data = {}
        display.printToTerm("This setup will configure the AWS Config file located in: app")
        s3Bucket = display.askUser("What is your S3 Bucket Name?")
        data['s3BucketName'] = s3Bucket
        print(data)
        dataManage.saveConfigJSONFile(data, "VerizonRESTConfig")
       
	 '''
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

        '''

setup()



########################################
## Runs api config setup
#######################################
def setupAPIConfig():
	print("This setup will configure the VerizonRESTConfig.json file located in: app/config/VerizonRESTConfig.json \n")
	models.createRestAPIConfigFile()
	RESTENDPOINT = view.getUserInput("What is your REST API Endpoint? Ex. 'https://api.networkfleet.com/'\n>")
	models.setVehicleRESTAPIData("REST_API_ENDPOINT", RESTENDPOINT)
	getAuthentication()
	getGroups()
	print("OK - SETUP FOR VERIZON REST MODULE COMPLETE")




#############################################
## Related to setup
## Sets API token
#############################################
def getAPIToken(restEndpoint,username, password):
	
	url = restEndpoint
	payload = "grant_type=password&username="+username+"&password="+password
	headers = {
    	'Content-Type': "application/x-www-form-urlencoded",
    	'Cache-Control': "no-cache",
    
    	}
	
	response = requests.request("POST", url, data=payload, headers=headers)
	response = json.loads(response.text)
        models.setVehicleRESTAPIData("REST_API_KEY", response["access_token"])
	models.setVehicleRESTAPIData("REST_API_KEY_REFRESH", response["refresh_token"])
	models.setVehicleRESTAPIData("REST_API_KEY_TYPE", response["token_type"])
	models.setVehicleRESTAPIData("REST_API_KEY_TIMEOUT", response["expires_in"])
################################################
## Gets rest API data
## Returns data in json format
################################################
def getRESTData(restEndpointURL, endpoint, restKey, restKeyType):
	url = restEndpointURL+endpoint

	headers = {
    	'Authorization': restKeyType+" "+restKey,
    	'Accept': "application/vnd.networkfleet.api-v1+json",
    	'Content-Type': "application/vnd.networkfleet.api-v1+json",
    	'Cache-Control': "no-cache",
    	
    	}

	response = requests.request("GET", url, headers=headers)

	
	return (response.json())

################################################
## Related to Set up
## gets the group ID
################################################
def getGroupID(GroupName, jsonData):
	for Group in jsonData["group"]:
		#print(Group)
		if Group["name"] == GroupName:
			return Group["@id"]
##################################################
## Related to set up scripts
## Gets authenticatiopn for the Veizon rest API
##################################################
def getAuthentication():
        REST_API_AUTH_ENDPOINT = view.getUserInput("What is your Authentication point? Ex. https://auth.networkfleet.com/token \n>")
        models.setVehicleRESTAPIData("REST_API_AUTH_ENDPOINT", REST_API_AUTH_ENDPOINT)
        REST_API_USERNAME = view.getUserInput("What is your REST API UserName? \n>")
        models.setVehicleRESTAPIData("REST_API_USERNAME", REST_API_USERNAME)
        REST_API_PASSWORD = getpass.getpass('What is your REST API Password?:\n>')
        models.setVehicleRESTAPIData("REST_API_PASSWORD", REST_API_PASSWORD)
	getAPIToken(models.getVehicleRestAPIData("REST_API_AUTH_ENDPOINT"), models.getVehicleRestAPIData("REST_API_USERNAME"), models.getVehicleRestAPIData("REST_API_PASSWORD"))
        getRESTData(models.getVehicleRestAPIData("REST_API_ENDPOINT"),"locations", models.getVehicleRestAPIData("REST_API_KEY"),models.getVehicleRestAPIData("REST_API_KEY_TYPE"))
##################################################
## Related to set up scripts
## Sets the group ID used for the App
################################################## 
def getGroups():

	jsonDATA = getRESTData(models.getVehicleRestAPIData("REST_API_ENDPOINT"),"groups", models.getVehicleRestAPIData("REST_API_KEY"),models.getVehicleRestAPIData("REST_API_KEY_TYPE"))
	view.displayJSON(jsonDATA, "group", "name")
        groupName = view.getUserInput("What group do you want to track?")
        groupID = getGroupID(groupName, jsonDATA)
        models.setVehicleRESTAPIData("REST_VEHICLE_GROUP", groupID)
#####################################################
## Runs the setup scripts
#####################################################
def setup():
	Exists = models.createRestAPIConfigFile()
	if(not Exists):
		setupAPIConfig()
setup()















