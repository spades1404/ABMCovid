from ABMC19.Agents.Actions.Pathfinding.grabNeighbourCoords import grabNeighbouringCells
from ABMC19.Agents.Actions.Pathfinding.findPossiblePaths import nearestThreeCoord
def moveAgent(agent):
    #first lets find all the cells i can move to
    #then lets narrow it down to the nearest 3 - since only 3 cells will ever be the in the direction of travel
    #then we will decide if it is efficient to move or not
    #then we will move accordingly
    #then we will check what cell we are at in case the path position changes

    neighbours = grabNeighbouringCells(agent,True) #getting neighbours
    destinationCoord = ()

    if agent.movementDir == 0:
        destinationCoord = agent.workCoord
    elif agent.movementDir == 1:
        destinationCoord = agent.homeCoord

    possibleMoves = nearestThreeCoord(neighbours,destinationCoord)
    filteredMoves = [i for i in possibleMoves if agent.model.grid.get_cell_list_contents([i]) == []] # we are filtering cells that are filled

    if filteredMoves == []: #if there are no logical moves do nothing
        return
    else:
        agent.model.grid.move_agent(agent,filteredMoves[0]) #move to the first availiable spot
