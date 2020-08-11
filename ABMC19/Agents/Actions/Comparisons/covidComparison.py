from ABMC19.Agents.Actions.Comparisons.grabNeighbourAgents import *
from ABMC19.Agents.Actions.Comparisons.otocomparison import *

'''
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
'''

def covidComparison(agent): #this could use a change around at some point
    #if they are at any building only check one cell
    if agent.pos in agent.model.fullCoords : #if agent is in any building
        for i in grabNeighboursOneCell(agent): #for each one agents in the building compare
            otoc(agent,
                 i,
                 sameLocation= True,
                 hospital= [True if agent.pos in [[j for j in i.location] for i in agent.model.allSpecialAreas["hospitals"]] else False],
                 workplace= [True if agent.pos in [[j for j in i.location] for i in agent.model.workplaces] else False],
                 dirtyCell= [True if agent.pos in [i[0] for i in agent.model.dirtyCells] else False]
                 )
    else: #if check aruond them too
        for i in grabNeighboursAgents(agent,False):
            otoc(
                agent,
                i,
            )
        for i in grabNeighboursOneCell(agent):
            otoc(
                agent,
                i,
                sameLocation=True
            )


    return

