from ABMC19.Agents.Actions.Pathfinding.grabNeighbourCoords import grabNeighbouringCells
from ABMC19.Agents.Actions.Pathfinding.findPossiblePaths import nearestXCoords, nearestOneCoords
from ABMC19.Agents.Actions.Pathfinding.updateDirection import updateMovementDirection
from ABMC19.Agents.Actions.Pathfinding.grabDestCoord import grabDestCoord



def moveAgent(agent): #THIS IS ONLY FOR PATHFINDING AND MOVING - IVE SEPARATED ALL CONNECTIONS TO CHANGING MOVEMENT PATHS
    grabDestCoord(agent)  # updates the agents destination coord
    neighbours = grabNeighbouringCells(agent,False) #getting neighbouring cells

    if agent.currentDestCoord in neighbours: #if we are in range of the destination coordinate just move there rather doing other calculations
        agent.model.grid.move_agent(agent, agent.currentDestCoord)
        return


    possibleMoves = nearestXCoords(neighbours, agent.currentDestCoord, 3)  # finding the best possible moves
    filteredMoves = [i for i in possibleMoves if agent.model.grid.get_cell_list_contents([i]) == []] # we are filtering cells that are filled

    if filteredMoves == []: #if no logical moves just do the first availiable thing
        agent.model.grid.move_agent(agent,nearestOneCoords(possibleMoves,agent.currentDestCoord))
        return
    else:#move to the closest one
        agent.model.grid.move_agent(agent,filteredMoves[0])
        return


