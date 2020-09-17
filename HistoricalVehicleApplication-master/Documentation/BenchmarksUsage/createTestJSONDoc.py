import json
dataHold = {}
data = {}
for i in range(5500):
    data = {"CITYST_ID": i, "Data": {"name": str('James'+str(i)), 'Cordinates': [[100.32, 99.23], [80.443, 40.2222], [40.111, 22.231],[100.32, 99.23], [80.443, 40.2222], [40.111, 22.231]]}}

    dataHold[i]= data
with open('dataHold.json', 'w') as outfile:  
    json.dump(dataHold, outfile)
