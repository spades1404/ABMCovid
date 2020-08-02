from ABMC19.Model.CoordinateScripts.generateRandomUniqueCoordinates import gruc

class aoi:
    def __init__(self,
                 model,
                 capacity = None):
        self.capactiy = capacity #Static
        self.currentCapacity = capacity #Tracker
        self.location = gruc(model,1)[0] #tuple
