from ABMC19.Agents.Actions.Comparisons.grabNeighbourAgents import *
from ABMC19.Agents.Actions.Comparisons.otocomparison import *
def covidCompare(agent):
    if agent.pos == agent.homeCoord or agent.infected == True: #if they are at home then they shouldnt be able to contract the virus or if they are already infected they cant get infected again
        return
    #first lets get agents in our immediete area (i will use 4 surrounding cells - can later be changed to 8)

    neighbours = grabNeighboursAgents(agent,False)

    #next for each agent lets run a comparison for if they are infected etc. An outcome of true means that we have been infected

    if neighbours == []:
        return
    for i in neighbours:
        onetoonecomparison(agent,i)





