from ABMC19.Agents.Actions.Pathfinding.findPossiblePaths import nearestOneCoords

def grabDestCoord(agent):
    #using a switch statement here
    '''
    swticher = {
        0 : agent.work.location,
        1 : agent.home.location,
        2 : nearestXCoords([i.location for i in agent.model.allSpecialAreas["shops"]][0], agent.pos, 1),
        3 : nearestXCoords([i.location for i in agent.model.allSpecialAreas["gyms"]][0], agent.pos, 1),
        4 : nearestXCoords([i.location for i in agent.model.allSpecialAreas["hospitals"]][0], agent.pos, 1)
    }

    agent.currentDestCoord = swticher.get(agent.movementDir)
    '''
    x = agent.movementDir
    if x == 0:
        agent.currentDestCoord = agent.work.location
    elif x == 1:
        agent.currentDestCoord = agent.home.location
    elif x == 2:
        agent.currentDestCoord = nearestOneCoords([i.location for i in agent.model.allSpecialAreas["shops"]], agent.pos)
    elif x == 3:
        agent.currentDestCoord = nearestOneCoords([i.location for i in agent.model.allSpecialAreas["misc"]], agent.pos)
    elif x == 4:
        agent.currentDestCoord = nearestOneCoords([i.location for i in agent.model.allSpecialAreas["hospitals"]], agent.pos)