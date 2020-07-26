from ABMC19.Agents.Actions.Pathfinding.grabNeighbourCoords import grabNeighbouringCells
from ABMC19.Agents.Actions.Pathfinding.findPossiblePaths import nearestThreeCoord
from ABMC19.Agents.characteristics import hubDef
import random
def moveAgent(agent):
    #first lets find all the cells i can move to
    #then lets narrow it down to the nearest 3 - since only 3 cells will ever be the in the direction of travel
    #then we will decide if it is efficient to move or not
    #then we will move accordingly
    #then we will check what cell we are at in case the path position changes

    #if agent.distanced == True: # If the agent is social distancing, remain stationary
    #    return

    neighbours = grabNeighbouringCells(agent,True) #getting neighbours
    destinationCoord = ()
    location = hubDef()     # Determines movementDir after homeCoord

    if agent.movementDir == 0:
        destinationCoord = agent.workCoord
    elif agent.movementDir == 1:
        destinationCoord = agent.homeCoord
    elif agent.movementDir == 2:
        destinationCoord = agent.hubCoord

    possibleMoves = nearestThreeCoord(neighbours,destinationCoord)
    filteredMoves = [i for i in possibleMoves if agent.model.grid.get_cell_list_contents([i]) == []] # we are filtering cells that are filled

    if filteredMoves == []: # If there are no logical moves, go home/work to avoid buggy clusters around hubs
        agent.movementDir = random.randint(0,1)
    else:
        agent.model.grid.move_agent(agent,filteredMoves[0]) #move to the first availiable spot
        if filteredMoves[0] == agent.workCoord:
            agent.movementDir = 1
        elif filteredMoves[0] == agent.homeCoord:
            agent.movementDir = location    # Go from home to work OR from home to a central hub
        elif filteredMoves[0] == agent.hubCoord:
            agent.movementDir = 1   # Go home after going to a central hub
