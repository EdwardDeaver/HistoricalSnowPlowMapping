import json

def createJSONFile(Data, SaveLocation, FileName):
	with open(SaveLocation+FileName+".json", 'w') as outfile:
    		json.dump(Data, outfile)
