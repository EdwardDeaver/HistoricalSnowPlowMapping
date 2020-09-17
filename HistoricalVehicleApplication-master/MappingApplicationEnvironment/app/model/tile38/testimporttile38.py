import interactWithTile38

#print(interactWithTile38.startTile38())

#try:
client = interactWithTile38.connectToTile38("127.0.0.1")
#print(client)
#print("import print test")
print(interactWithTile38.loadGeoFences(client, "amqp://guest:guest@localhost:5672/warehouse", "TRYCATCHTESTER", [[[-72, 46], [-73,42],[-73, 46], [-72, 46]]]))
returnedData = interactWithTile38.setFleetLocation(client, "truck21Test", "42", "76")
print(returnedData)
