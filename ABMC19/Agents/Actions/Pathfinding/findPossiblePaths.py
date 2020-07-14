#im going to use a spatial tree for this
#there might be a better way
from scipy import spatial

def nearestThreeCoord(possibleMoves,destination):

    tree = spatial.KDTree(possibleMoves)
    listPositions = tree.query([destination],k=3) #returns the list positions of the 3 nearest coords
    return [possibleMoves[i] for i in list(listPositions[1][0])] # there is a bunch of weird formats scipy returns so this one line removes them all and returns the coords


