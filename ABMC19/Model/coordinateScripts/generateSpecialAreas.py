#This script will handle creating workplaces and hospitals


#### THIS IS DEPRECATED NO LONGER NEEDED####
from ABMC19.Model.CoordinateScripts.generateRandomUniqueCoordinates import gruc
import random
def generateSpecialCoordinates(model):
    numOfCoords = model.numAgents * 2
    listOfCoords = gruc(model,numOfCoords)
    pairedCoord = [[i, k] for i, k in zip(listOfCoords[0::2],listOfCoords[1::2])] #going to package them as a list of lists. Where each value is [workplacecoord , homecoord]
    return pairedCoord



