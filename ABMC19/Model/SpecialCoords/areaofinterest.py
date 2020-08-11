from ABMC19.Model.CoordinateScripts.generateRandomUniqueCoordinates import gruc,tetromino
import random

class aoi:
    def __init__(self,
                 model,
                 capacity = None,
                 oneCell = True):
        self.capacity = capacity #Static
        self.currentCapacity = capacity #Tracker
        self.oneCell = oneCell #if the object is bigger than one cell or not
        if oneCell == True:
            self.location = [gruc(model,1)[0]] #tuple
        else:
            self.location = tetromino(model)


    def returnType(self):
        print(type(self))