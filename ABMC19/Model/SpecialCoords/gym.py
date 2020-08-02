from ABMC19.Model.SpecialCoords.areaofinterest import *

class Gym(aoi):
    def __init__(self,model):
        super(Gym, self).__init__(capacity=100,model=model)
