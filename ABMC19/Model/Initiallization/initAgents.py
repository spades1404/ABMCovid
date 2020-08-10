from ABMC19.Agents.agent import covAgent
from itertools import cycle
import random

def generateAgents(model): #This function will generate homes and houses
    numAgents = model.numAgents
    numHouses = random.randint(round(numAgents/2),numAgents)

    houses = cycle(model.allSpecialAreas["houses"])
    workplaces = cycle(model.workplaces)


    for i in range(numAgents):

        house = next(houses)
        workplace = next(workplaces)
        agent = covAgent(i,model,house,workplace)

        house.inhabitants.append(agent)

        model.agents.append(agent)
        model.grid.place_agent(agent,(random.randint(0,model.gridWidth-1),random.randint(0,model.gridWidth-1))) #placing them somewhere random
        model.schedule.add(agent)



