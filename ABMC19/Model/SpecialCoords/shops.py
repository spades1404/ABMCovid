from ABMC19.Model.SpecialCoords.areaofinterest import *

class Shop(aoi):
    def __init__(self,model):
        super(Shop, self).__init__(capacity=300,model=model,oneCell=False)
