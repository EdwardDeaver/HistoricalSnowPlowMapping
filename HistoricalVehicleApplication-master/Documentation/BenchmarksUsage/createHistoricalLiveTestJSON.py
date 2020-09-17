import json
dataHold = {}
data = {}
for i in range(5500):
    data = {"CITYST_ID": i, "Data": {"Plow Time": "17:13:48.652740516", "Plow Date": "2018-07-17", "Plow Type": "Plowing"}}

    dataHold[i]= data
with open('snapshotTestJSON.json', 'w') as outfile:  
    json.dump(dataHold, outfile)
