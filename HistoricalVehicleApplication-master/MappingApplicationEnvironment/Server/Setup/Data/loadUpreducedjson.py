
import json
with open('dataOfReducedFile.json') as json_data:
    d = json.load(json_data)

for feature in d:
    print(feature)
    print (feature["CITYST_ID"])
    print (feature["coordinates"])
