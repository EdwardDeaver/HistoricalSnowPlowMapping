##############################
## Setup
##############################
import models
import view



#####################################################
## Set's up json doc with information
#####################################################
def setupAPIConfig():
        print("This setup will configure the geocoding_rest_api.json file located in: app/static/ \n")

        COUNTRY_ORIGIN = view.getUserInput("What country is this being setup in? Ex. USA[United States], CA[Canada], MX[Mexico]\n>")
        models.setGeoCodeAPIData("COUNTRY_ORIGIN", COUNTRY_ORIGIN)

        STATE_ORIGIN = view.getUserInput("What state is this being setup for? Ex. California, Wisconson, New York\n>")
        models.setGeoCodeAPIData("STATE_ORIGIN", STATE_ORIGIN)

        CITY_ORIGIN = view.getUserInput("What city is this being setup for? Ex. Los Angels, Madison, Syracuse\n>")
        models.setGeoCodeAPIData("CITY_ORIGIN", CITY_ORIGIN)

        REST_END_POINT = view.getUserInput("What is your REST API Endpoint? Ex. 'https://www.mapquestapi.com/'\n>")
        models.setGeoCodeAPIData("REST_API_ENDPOINT", REST_END_POINT)

        REST_API_KEY = view.getUserInput("What is your REST GEOCODE API KEY?\n>")
        REST_API_KEY = REST_API_KEY.split(",")
        models.setGeoCodeAPIData("REST_API_KEY", REST_API_KEY)

        REST_API_SECRET = view.getUserInput("What is your REST GEOCODE API SECRET?\n>")
        models.setGeoCodeAPIData("REST_API_SECRET", REST_API_SECRET)


######################################
## Creates the setup for the geocode API
######################################
def setup():

        Exists = models.createGeoCodeAPIConfigFile()
        if(not Exists):
                setupAPIConfig()

