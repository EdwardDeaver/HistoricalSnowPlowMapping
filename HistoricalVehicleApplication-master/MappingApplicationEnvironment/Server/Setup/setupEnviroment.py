#!/usr/bin/python3
import sys
import subprocess
def main():

	depedencyCheck()
	# Need cath to if it's not
	print("The System Will now check if the required packages are installed")
	
####################################
## Obatin SYSTEM INFORMATION
## Reason: The application needs system information to use the package manager
## Sets OS data
####################################

'''
def getSystemInformation():
	try:
		obtainOS = subprocess.check_output(["cat", "/etc/os-release"])
	except:
		print("Your OS can not be determined")
		getUserInfo("What OS are you using?")	
		checkUserInput(userInput, "What OS are you using")		

	for line in obtainOS.splitlines():
		readLines = line.decode("utf-8")	
		readLines = readLines.split("=")
		if(readLines[0] == "ID"):	
			global OS_NAME
			OS_NAME = readLines[1]
			global OS_PACKAGE_MANAGER
			OS_PACKAGE_MANAGER = OSDETAILS.get(OS_NAME)
			print("Package Manager: ")
			print(OS_PACKAGE_MANAGER)
		if(readLines[0] == "VERSION_ID"):
			print(readLines[1])
			OS_VER_NUMBER = readLines[1]		
'''
			
####################################
## Confirm or Deny Message
## Reason: Need y or n 
## Returns: True[y] or False[n]
####################################]
def confirmOrDeny(Message):
	response = getUserInfo(Message)
	while (response != "y") and (response !=  "n"):
		response = getUserInfo(Message)
	if(response== "y"):
		return True
	if(response=="n"):
		return False	
def install():

	subprocess.check_output(["sudo", "apt", "update"])
#####################################
## Will check if dependencies are installed
#####################################
def depedencyCheck():
	PythonVersion =  sys.version_info
	
	Python3 = subprocess.check_output(["cat", "/etc/os-release"])
main()
