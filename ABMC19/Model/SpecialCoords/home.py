from ABMC19.Model.SpecialCoords.areaofinterest import *

class Home(aoi):

    def __init__(self,model):
        super(Home, self).__init__(model=model) #Not Using The Capacity Variable
        self.inhabitants = []
