#This script will handle creating workplaces and hospitals

from ABMC19.Model.coordinateScripts.generateRandomCoord import *
def generateSpecialCoordinates(model):
    numOfCoords = model.numAgents * 2
    maxX = model.gridWidth - 1
    maxY = model.gridHeight - 1

    listOfCoords = []

    for i in range(numOfCoords):
        listOfCoords.append(generateCoordinate(listOfCoords,maxX,maxY))

    pairedCoord = []
    #going to package them as a list of lists. Where each value is [workplacecoord , homecoord]

    for i, k in zip(listOfCoords[0::2], listOfCoords[1::2]):
        pairedCoord.append([i,k])

    return(pairedCoord)



