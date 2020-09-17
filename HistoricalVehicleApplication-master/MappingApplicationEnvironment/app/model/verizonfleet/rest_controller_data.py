
import getpass
import pprint
import requests
import json
### Internal Imports
import view
import models
import controllers
###########################################
## Command to get vehicle locations
## This is meant to be a public facing method so you can just get the reponse of vehicles
## Using Flag: KeyOn == True this means the vehicle is ON
## Returns [] with {} inside
############################################
def getVehicleLocations(sort):
        jsonResponse = controllers.getRESTData(models.getVehicleRestAPIData("REST_API_ENDPOINT"),"locations?for-group="+str(models.getVehicleRestAPIData("REST_VEHICLE_GROUP")), models.getVehicleRestAPIData("REST_API_KEY"),models.getVehicleRestAPIData("REST_API_KEY_TYPE"))
        if sort:
                sortedlist = []
                for holder in jsonResponse["gpsMessage"]:
                        if(holder["keyOn"] == True):
                                sortedlist.append(holder)

                return sortedlist
        return jsonResponse
print(getVehicleLocations(False))
