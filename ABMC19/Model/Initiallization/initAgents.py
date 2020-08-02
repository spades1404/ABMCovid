from ABMC19.Agents.agent import covAgent
from ABMC19.Model.SpecialCoords.home import Home
from ABMC19.Model.CoordinateScripts.generateRandomUniqueCoordinates import gruc
from itertools import cycle
import random

def generateAgents(model): #This function will generate homes and houses
    numAgents = model.numAgents
    numHouses = random.randint(round(numAgents/2),numAgents)

    houses = []
    for i in range(numHouses):
        houses.append(Home(model))

    model.allSpecialAreas["houses"] = [i for i in houses]
    houses = cycle(houses)
    workplaces = cycle(model.workplaces)


    for i in range(numAgents):

        if i < model.currentInfected:  # if i is less then the number of infected agents...
            infectedAgent = True  # then make the next agent infected at start
        else:
            infectedAgent = False

        house = next(houses)
        workplace = next(workplaces)
        agent = covAgent(i,model,house,workplace,infectedAgent)

        house.inhabitants.append(agent)

        model.agents.append(agent)
        model.grid.place_agent(agent,agent.work.location)
        model.schedule.add(agent)



