from ABMC19.Agents.Actions.Pathfinding.grabNeighbourCoords import grabNeighbouringCells
from ABMC19.Agents.Actions.Pathfinding.findPossiblePaths import nearestXCoords, nearestOneCoords
from ABMC19.Agents.Actions.Pathfinding.updateDirection import updateMovementDirection
from ABMC19.Agents.Actions.Pathfinding.grabDestCoord import grabDestCoord
def moveAgent(agent):
    #first lets find all the cells i can move to
    #then lets narrow it down to the nearest 3 - since only 3 cells will ever be the in the direction of travel
    #then we will decide if it is efficient to move or not
    #then we will move accordingly
    #then we will check what cell we are at in case the path position changes

    if doWeMove(agent) == False: return #checks if we should move or not
    neighbours = grabNeighbouringCells(agent,False) #getting neighbours
    #destinationCoord = grabDestCoord(agent) #getting our dest
    possibleMoves = nearestXCoords(neighbours,agent.currentDestCoord,3) #finding the best possible moves
    filteredMoves = [i for i in possibleMoves if agent.model.grid.get_cell_list_contents([i]) == []] # we are filtering cells that are filled

    if filteredMoves == []: #if no logical moves just do the first availiable thing
        agent.model.grid.move_agent(agent,nearestOneCoords(possibleMoves,agent.currentDestCoord))
    else:
        agent.model.grid.move_agent(agent,filteredMoves[0])
        updateMovementDirection(agent) #updates the agents movement dir if needed
        grabDestCoord(agent) #updates the agents destination coord


def doWeMove(agent):
    if agent.pos in [i.location for i in agent.model.allSpecialAreas["hospitals"]] and agent.hospitalized == True:
        return False
    elif agent.pos == agent.home.location and agent.isolating == True:
        return False
