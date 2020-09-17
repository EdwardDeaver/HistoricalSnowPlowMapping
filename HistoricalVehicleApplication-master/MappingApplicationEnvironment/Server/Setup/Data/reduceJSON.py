
import json
import pygeoj
testfile = pygeoj.load("City_Streets_2011.geojson")
totalDictionary = []
for feature in testfile:
    holdDictionary = {}
    holdingCordinates = []
    ############
    ## Swaps the cordinates due to geojson flipping them
    ############
    for i in feature.geometry.coordinates:
        holdingCordinates.append([i[1], i[0]])
                                 
    holdDictionary = {"CITYST_ID":feature.properties["CITYST_ID"],  "CORD": holdingCordinates}
    totalDictionary.append(holdDictionary)

with open('../../../Client/Data/Cords.json', 'w') as outfile:
    json.dump(totalDictionary, outfile, separators=(',', ':'))
