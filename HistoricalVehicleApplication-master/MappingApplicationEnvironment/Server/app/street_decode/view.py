###################
## This is the view it gets information from the user
###################
##################
## Made by: Edward C. Deaver, IV
#################

################
## Get User Information
###############

def getUserInput(Message):
	userInput = raw_input(Message)
	return userInput

def getYN(Message):
	try:
		userResponse = getUserInput(Message)
		if((userResponse != "y") or (userResponse != "n")):
			ValueError("invalid default answer: '%s'" % default)
		else:
			return userResponse 
	except ValueError:
		getYN(Message)


def kmlFileLocationPrep():
  	print("This setup will setup create your Streets.JSON file. Stored at ../static/streets/* \n")
        print("At this time please place your 'streets.KML' file in ../data/streets/\n")
        print("Using SCP: scp -r -i YourPrivateKey.pem streets.kml $USERNAME@SERVERIPADDRESS:/home/ec2-user/HistoricalVehicleApplication/MappingApplication/Server/app/data/streets/\n ")

	print("Checking for 'streets.kml'")

def displayJSON(Message, Field, subField):
	if (Field == ""):
		print(Message)
	else:
		for i in Message[Field]:
			print(i[subField])

