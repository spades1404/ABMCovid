import random
from ABMC19.Agents.Actions.Progression.removeAgentFromModel import removeAgentFromModel

def selfCheck(agent):
    tsi = agent.ticksSinceInfection

    if agent.infected == True:
        agent.ticksSinceInfection += 1

    if agent.progression == 1:
        agentProbability = tsi/14 * random.uniform(0.5,1.5) #converting into a decimal for randomness, odds get higher over days, will definetly do some proper statistics later
        if agentProbability> 0.5:
            agent.progression = 2 #they are now symptomatic

    if agent.progression == 2:
        agentProbability = tsi/28 * random.uniform(0.5,1.5) #probability of an event happening on this day
        if agentProbability > 0.5:
            lifeORdeath = random.uniform(0,1)
            #going to say there is a 10 percent chance you die
            if lifeORdeath > 0.1 :
                agent.progression = 3
                agent.infected = False
                agent.immune = True # may make this random
                agent.model.immune += 1
            else:
                agent.progression = 3
                agent.dead = True
                agent.model.deaths += 1
                removeAgentFromModel(agent)


