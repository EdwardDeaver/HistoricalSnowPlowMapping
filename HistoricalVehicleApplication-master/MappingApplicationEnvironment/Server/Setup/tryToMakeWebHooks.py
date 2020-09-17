import subprocess
import json

OS_NAME = ""
OS_VER_NUMBER = ""
OS_PACKAGE_MANAGER = ""

def main():
	print("Getting OS INFORMATION")
	getSystemInformation()

## Obatin SYSTEM INFORMATION
## Reason: The application needs system information to use the package manager
## Sets OS data
####################################
def getSystemInformation():
	obtainOS = subprocess.check_output(["", "/etc/os-release"])
	print(type(obtainOS))
	for line in obtainOS.splitlines():
		readLines = line.decode("utf-8")	
		readLines = readLines.split("=")
		if(readLines[0] == "ID"):
			print(readLines[1])
			OS_NAME = readLines[1]
		if(readLines[0] == "VERSION_ID"):
			print(readLines[1])
			OS_VER_NUMBER = readLines[1]		
		print(readLines)	

def getOSPackageManager():
		
	
def install():

	subprocess.check_output(["sudo", "apt", "update"])

main()
