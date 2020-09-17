import sys
sys.path.append('../')
#import json
import boto3
from model import dataManage
import time
from decimal import *

def loadInitialStreetDataToDB(StreetData):
        streetDataFile = dataManage.getData("streets_GEOJSON", "", True)
        dataManage.uploadToDynamo("StreetData", streetDataFile)
	#print("___________+_+_+_++_++____________________________________")
        #print("___________+_+_+_++_++____________________________________")
	#for i in streetDataFile["features"]:
       	#	if("I 690" in i["properties"]["FULLNAME"]):
        #                print("none")
        #        elif("I 81" in i["properties"]["FULLNAME"]):
        #                print("none")
        #        elif("I 481" in i["properties"]["FULLNAME"]):
        #                print(" ")
        #        else:
        #                print(i["properties"]["FULLNAME"])
        #                print(i["properties"]["CITYST_ID"])


def loadPolygonsToTile38():
		
def main():
	response = dataManage.createTables("HistoricalVehicleRecord")
	responseStreets = dataManage.createTables("StreetData")
	time.sleep(10)
	loadInitialStreetDataToDB("")
main()
