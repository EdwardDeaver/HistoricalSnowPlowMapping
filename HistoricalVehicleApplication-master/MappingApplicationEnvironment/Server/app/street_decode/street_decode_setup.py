import sys
sys.path.insert(0, '../')
from  street_decode import controllers as controller


def setup():
        controller.setupGeoJSON()
        controller.stripGeoJSONToCords()

