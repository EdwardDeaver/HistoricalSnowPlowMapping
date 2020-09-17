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


def displayJSON(Message, Field, subField):
	if (Field == ""):
		print(Message)
	else:
		for i in Message[Field]:
			print(i[subField])

