#im going to use a spatial tree for this
#there might be a better way
from scipy import spatial
import numpy as numpy


#NOTE THIS FUNCTION DOESNT WORK WHERE K = 1 , USE THE ONE BELOW FOR K = 1
def nearestXCoords(possibleMoves,destination, k): #updated this so you can do any amount of nearest coords

    if len(possibleMoves) == 1:
        return possibleMoves[0]
    tree = spatial.KDTree(possibleMoves)
    listPositions = tree.query([destination],k=k)[1] #returns the list positions of the 3 nearest coords

    #fixing stupid scipy formats
    old = []
    while type(listPositions) != numpy.int32:
        old = listPositions
        listPositions = listPositions[0]
    listPositions = list(old)


    return [possibleMoves[i] for i in list(listPositions)] # there is a bunch of weird formats scipy returns so this one line removes them all and returns the coords

def nearestOneCoords(possibleMoves,destination):
    if len(possibleMoves) == 1:
        return possibleMoves[0]
    tree = spatial.KDTree(possibleMoves)
    listPositions = tree.query([destination], k=1)[1]  # returns the list positions of the 3 nearest coords

    #fixing stupid scipy formats
    old = []
    while type(listPositions) != numpy.int32:
        old = listPositions
        listPositions = listPositions[0]
    listPositions = list(old)


    return possibleMoves[(listPositions[0])]

##NOTE TO SELF - SCIPY FORMATS ARE LITERALLY THE WORST THING EVER
