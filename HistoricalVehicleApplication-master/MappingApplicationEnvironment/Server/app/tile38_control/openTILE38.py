import os, sys
import subprocess
import model
def start_tile38():	
	os.chdir("../dependencies/tile38-1.12.3-linux-amd64/")
	subprocess.Popen(['nohup', './tile38-server', '-q', '&'])
	os.chdir("../../tile38_control/")
	PID = subprocess.check_output(['pgrep', '-o', '-x', 'tile38-server'])
	print ( PID)
	if(model.doesConfigFileExist()):
		print("Config Exists")
		model.setConfigFileData("TILE38_PID", PID)
start_tile38()
