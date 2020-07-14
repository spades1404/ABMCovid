import random

#just generates some coords when given a list of existing coords (special use case)
def generateCoordinate(existingCoords,XupperLim,YlowerLim):
    while True:
        coord = (random.randint(0,XupperLim),random.randint(0,YlowerLim))
        if coord not in existingCoords:
            return (coord)

