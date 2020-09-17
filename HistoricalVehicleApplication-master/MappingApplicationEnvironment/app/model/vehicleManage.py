from .verizonfleet import getData
###################

def getVehicleLocations(vehicleGroupName, apiKey, apiKeyType):
	apiEndPoint = "https://api.networkfleet.com/"
	#"locations?for-group="+vehicleGroupName
	apiResponse = getData.queryAPI("GET",apiEndPoint,"locations?for-group="+vehicleGroupName+"&limit=1000",apiKey,apiKeyType,"", "", "")
	return apiResponse
def refreshToken(refreshKey, username, password):
	url = "https://auth.networkfleet.com/"
	payload = "grant_type=refresh_token&refresh_token="+refreshKey
	apiResponse = getData.queryAPI("POST",url,"token","","",payload, username, password)
	return apiResponse
def validateAPI(username, password):
	url = "https://auth.networkfleet.com/"
	payload = "grant_type=password&username="+username+"&password="+password
	apiResponse = getData.queryAPI("POST",url,"token","","",payload, username, password)
	return apiResponse
#print(refreshToken("ab1275cf-f1db-42de-a579-89c6e21495ba", "Edeaver", "6e691d92eec0a4dcc821370ec0a9a52f"))
#print(getVehicleLocations("https://api.networkfleet.com/", "415282", "4060b6c8-7cd3-40be-ba78-13e9492fdf15", "Bearer"))
