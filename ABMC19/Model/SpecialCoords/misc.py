from ABMC19.Model.SpecialCoords.areaofinterest import *

class Misc(aoi): #THESE ARE miscellaneous AREAS LIKE GYMS, RESTAURANTS, ETC
    def __init__(self,model):
        super(Misc, self).__init__(capacity=100,model=model)
