import  view
import  models
import control_decode_of_streets as decode_streets
import json
import os.path


def setupGeoJSON():

	url = view.getUserInput("Please provide a URL for your street map in GEOJSON format. Ex. 'https://opendata.arcgis.com/datasets/47cadd4fe5b344f895c5a3e672463899_0.geojson'\n>")
	models.downloadJSON(url, "streets_GEOJSON.json", "../static/streets/")
	
def stripGeoJSONToCords():
	strippedOut = []
	JSONLine  = {"CITYST_ID": 0, "CORD": 0}
	json = models.getJSON("streets_GEOJSON.json", "../static/streets/")	
	for i in json["features"]:
		JSONLine["CITYST_ID"] = i["properties"]["CITYST_ID"]
		tempCords = []
		for cords in i["geometry"]["coordinates"]:
			tempCords.append([cords[1], cords[0]])
		JSONLine["CORD"] = tempCords 
		strippedOut.append( {"CITYST_ID": i["properties"]["CITYST_ID"], "CORD": tempCords})
	models.exportJSON(strippedOut, "streets_GEOJSON2.json", "../static/streets/")


def setup():
	if(not os.path.isfile("../static/streets/streets_GEOJSON.json")):
        	setupGeoJSON()
        	stripGeoJSONToCords()
	if(not os.path.isfile("../static/streets/GEOCODED_STREET_DATA.json")):
		decode_streets.createGeoCodeJSON() 
setup()
