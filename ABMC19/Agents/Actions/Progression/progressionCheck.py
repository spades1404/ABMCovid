import random
from ABMC19.Agents.Actions.Progression.removeAgentFromModel import removeAgentFromModel
from ABMC19.Agents.characteristics import reinfectDef

def selfCheck(agent):
    tsi = agent.ticksSinceInfection
    if agent.infected == True:
        agent.ticksSinceInfection += 1
    if agent.progression == 1:
        if ((tsi/14)*random.uniform(0.8,1.2)) >= 1:  #this line uses a specific decimal. Its setup so any day 12+ has a chance of an event happening.
            agent.progression = 2
        else:
            return
    elif agent.progression == 2:
        if ((tsi/21)*random.uniform(0.7,1.3)) >= 1: #simmilar line to above - its active between 17-28 days. I choose 21 days as the median to base this off
            agent.progression = 3
            agent.model.infected -= 1
            x = bool(random.getrandbits(1)) #going to say its 50/50 that the

            cfr = random.uniform(0,1) #cfr is case fatality rate, im going of an avg of 5% cases result in death (however this can be alterable)

            if agent.obese == True:
                cfr += 0.25 #adds a % risk of death

            if cfr > 0.93: #~7% chance of death
                agent.model.deaths += 1
                agent.dead = True
                removeAgentFromModel(agent)
            else:
                agent.model.immune += 1
                agent.immune = True

    elif agent.progression == 3: #After agent becomes immune
        if random.uniform(0.6,1.4) >= 1: #Chance of reinfection
            if reinfectDef() == True:
                agent.immune = False #Agent becomes infected (True) or not (False)
                agent.model.immune -= 1 #Remove their value from datacollector
                agent.infected = False #Reset agent's infected and progression status
                agent.progression = 0
