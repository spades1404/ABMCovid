#This script will handle creating workplaces and hospitals
import random
def generateSpecialCoordinates(model):
    numOfCoords = model.numAgents * 2
    maxX = model.gridWidth
    maxY = model.gridHeight


    #for i in range(numOfCoords):
    #listOfCoords.append(generateCoordinate(listOfCoords,maxX,maxY))

    randintsX = range(0,maxX)
    randintsY = range(0,maxY)
    listOfCoords = set()
    while len(listOfCoords) < numOfCoords:
        listOfCoords.add((random.choice(randintsX),random.choice(randintsY)))
    listOfCoords = list(listOfCoords)
    pairedCoord = []
    #going to package them as a list of lists. Where each value is [workplacecoord , homecoord]

    for i, k in zip(listOfCoords[0::2], listOfCoords[1::2]):
        pairedCoord.append([i,k])

    return(pairedCoord)



