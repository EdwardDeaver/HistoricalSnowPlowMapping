import subprocess
import model
import view

def checkIfRabbitMQRunning():
	PID = subprocess.check_output(['pgrep', '-o', '-x', 'rabbitmq-server'])
	if(PID != ""):
		model.setConfigFileData("RABBITMQ_PID", PID)
		return True
	else:
		return False
def setup():
	if (checkIfRabbitMQRunning()):
        	if(not model.doesConfigFileExist()):
                	print("This setup will configure the RABBITMQ_Config.json file located in: app/config/RABBITMQ_Config.json \n")
                	model.createConfigFile()
        	if(model.doesConfigFileExist() and (model.getConfigFileData("RABBITMQ_ENDPOINT_URL") == "" or  model.getConfigFileData("RABBITMQ_USER") == "")):
                	RABBITMQ_ENDPOINT = view.getUserInput("What is the endpoint being used for RABBITMQ\n>")
	                model.setConfigFileData("RABBITMQ_ENDPOINT_URL", RABBITMQ_ENDPOINT)
        	        print("OK - RabbitMQ  COMPLETE")
		authentication()	
def authentication():
	try:
		try:
			delete_guest_user = subprocess.check_output(['sudo', 'rabbitmqctl', 'delete_user', 'guest'])
			print(delete_guest_user)
		except:
			print("GUEST")
		
		try:
			set_admin_user_pass = subprocess.check_output(['sudo', 'rabbitmqctl', 'add_user', 'MappingApplicationAdmin', 'TimeWarpMapping1848'])
			print(set_admin_user_pass)
                        print(subprocess.check_output(['sudo', 'rabbitmqctl', 'set_user_tags', 'MappingApplicationAdmin', 'administrator']))
			print(subprocess.check_output(['sudo', 'rabbitmqctl', 'set_permissions', '-p', '/', 'MappingApplicationAdmin', '".*"', '".*"', '".*"']))

		except:
			print("Admin set")
	
	except:
		print("ok")
	




