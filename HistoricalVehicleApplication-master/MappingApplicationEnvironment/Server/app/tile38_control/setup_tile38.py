import model
import view
import get_tile38 as getTile38
def setup():
        if(not model.doesConfigFileExist()):
	        print("This setup will configure the VerizonRESTConfig.json file located in: app/config/TILE38_Config.json \n")
		model.createConfigFile()
	if(model.doesConfigFileExist() and (model.getConfigFileData("TILE38_DOWNLOAD_URL") == "" or  model.getConfigFileData("TILE38_DOWNLOAD_URL") == "")):
		TILE38_DOWNLOAD_URL = view.getUserInput("What is the download url for Tile38? Ex. https://github.com/tidwall/tile38/releases/download/1.12.3/tile38-1.12.3-darwin-amd64.zip\n>")
		model.setConfigFileData("TILE38_DOWNLOAD_URL", TILE38_DOWNLOAD_URL)

	        TILE38_IP = view.getUserInput("What is your Tile38 Endpoint? Ex. 127.0.0.1\n>")
        	model.setConfigFileData("TILE38_ENDPOINT_URL", TILE38_IP)
        
		print("OK - TILE 38 COMPLETE")
	downloadTile38(model.getConfigFileData("TILE38_DOWNLOAD_URL"))
def downloadTile38(url):
	getTile38.download_file(url)



