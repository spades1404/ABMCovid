from ABMC19.Agents.Actions.Pathfinding.grabNeighbourCoords import grabNeighbouringCells
from itertools import chain

def contactedAgents(agent):



    if agent.infected == False:
        return
    elif agent.pos in list(chain.from_iterable([[[k for k in j.location] for j in agent.model.allSpecialAreas[i]] for i in agent.model.allSpecialAreas])):
        contacts = agent.model.grid.get_cell_list_contents(agent.pos)
        [agent.contacted.append(i) for i in contacts]
    else:
        contacts = [agent.model.grid.get_cell_list_contents([i]) for i in grabNeighbouringCells(agent,False,True) if i not in list(chain.from_iterable([[[k for k in j.location] for j in agent.model.allSpecialAreas[i]] for i in agent.model.allSpecialAreas]))]
        [agent.contacted.append(i) for i in contacts]

    #agent.contacted = list(chain.from_iterable(agent.contacted)) #Formats it into a nice 1D list

