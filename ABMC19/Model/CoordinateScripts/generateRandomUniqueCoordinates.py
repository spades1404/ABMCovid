import random

def gruc(model,numNewCoords): #use this to handle new coords added to the model smoothly
    maxX = model.gridWidth
    maxY = model.gridHeight

    # for i in range(numOfCoords):
    # listOfCoords.append(generateCoordinate(listOfCoords,maxX,maxY))


    randintsX = range(0, maxX)
    randintsY = range(0, maxY)
    fullCoords = set(model.fullCoords)
    newCoord = []


    x = len(fullCoords) #needs to be hear since while loop would iterate forever otherwise

    while len(fullCoords) < (numNewCoords+x):
        coord = (random.choice(randintsX), random.choice(randintsY))
        fullCoords.add(coord)
        newCoord.append(coord)


    model.fullCoords = fullCoords

    return newCoord