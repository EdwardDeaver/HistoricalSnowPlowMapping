import sys
sys.path.insert(0, '../')

from geocoding import controllers as geocoder

from street_decode import models as streetDecode



#####################################
## Creates GeoCoded JSON File
#####################################

def createGeoCodeJSON():
	geocodedInsert = []
	myStreetFile = streetDecode.getJSON("streets_GEOJSON.json", "../static/streets/")
	for featureSet in myStreetFile["features"]:
			
		 	print (str(featureSet["properties"]["L_T_ADD"])+" "+featureSet["properties"]["FULLNAME"])
			if((featureSet["properties"]["L_T_ADD"] == None) or (featureSet["properties"]["R_T_ADD"] == None) or (featureSet["properties"]["L_F_ADD"]== None) or (featureSet["properties"]["R_F_ADD"]==None)):
				continue
			if(featureSet["properties"]["FULLNAME"] == None):
				continue 
			##
			## CITYST_I: ## , L_T_ADD: [X, Y], R_T_ADD: [X, Y], L_F_ADD: [X, Y], R_F_ADD: [X, Y]
			##
			print(featureSet["properties"]["L_T_ADD"])
			print(featureSet["properties"]["R_T_ADD"])
			print(featureSet["properties"]["L_F_ADD"])
			print(featureSet["properties"]["R_F_ADD"])
			try:
				L_T_ADD = geocoder.geoCode(str(featureSet["properties"]["L_T_ADD"])+" "+featureSet["properties"]["FULLNAME"])
				print(L_T_ADD)	
				R_T_ADD = geocoder.geoCode(str(featureSet["properties"]["R_T_ADD"])+" "+featureSet["properties"]["FULLNAME"])
				print(R_T_ADD)
				L_F_ADD = geocoder.geoCode(str(featureSet["properties"]["L_F_ADD"])+" "+featureSet["properties"]["FULLNAME"])
				print(L_F_ADD)
				R_F_ADD = geocoder.geoCode(str(featureSet["properties"]["R_F_ADD"])+" "+featureSet["properties"]["FULLNAME"])
				print(R_F_ADD)
			except (ValueError, IndexError):
				exit('Ran out of keys to use')
			geocodedInsert.append({"CITYST_ID":  featureSet["properties"]["CITYST_ID"],"L_T_ADD": L_T_ADD, "R_T_ADD":R_T_ADD, "L_F_ADD":L_F_ADD, "R_F_ADD":R_F_ADD  })


	print(geocodedInsert)
	streetDecode.exportJSON(geocodedInsert, "GEOCODED_STREET_DATA.json", "../static/streets/")
			
			





