import random
from ABMC19.Agents.Actions.Progression.removeAgentFromModel import removeAgentFromModel

def selfCheck(agent):
    tsi = agent.ticksSinceInfection

    if agent.infected == True:
        agent.ticksSinceInfection += 1

    if agent.progression == 1:
        agentProbability = tsi/14 * random.uniform(1,1.5) #converting into a decimal for randomness, odds get higher over days, will definetly do some proper statistics later
        if agentProbability> 0.5:
            agent.progression = 2 #they are now symptomatic

    elif agent.progression == 2:
        agentProbability = tsi/28 * random.uniform(1,1.5) #probability of an event happening on this day
        if agentProbability > 0.5:

            agent.progression = 3
            agent.model.infected -= 1  # going to decrement the infection counter

            lifeORdeath = random.uniform(0,1)
            #going to say there is a 50 percent chance you die
            if lifeORdeath > 0.5 :
                agent.immune = True # may make this random
                agent.model.immune += 1

            else:
                agent.dead = True
                agent.model.deaths += 1
                removeAgentFromModel(agent)

def selfCheck2(agent):
    tsi = agent.ticksSinceInfection
    if agent.infected == True:
        agent.ticksSinceInfection += 1

    if agent.progression == 1:
        if tsi == 14:
            agent.progression = 2
    elif agent.progression == 2:
        if tsi == 21:
            agent.progression = 3
            agent.model.infected -= 1
            x = bool(random.getrandbits(1))

            if x == True:
                agent.model.deaths += 1
                agent.dead = True
            else:
                agent.model.immune+=1
                agent.immune = True


def newselfCheck(agent):
    tsi = agent.ticksSinceInfection
    if agent.infected == True:
        agent.ticksSinceInfection += 1
    #if agent.progression =