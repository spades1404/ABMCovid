import random
from ABMC19.Agents.Actions.Progression.removeAgentFromModel import removeAgentFromModel

def selfCheck(agent):
    bmi = random.normalvariate(27.5,7.5) # Normal distribution with mean as 27.5 and abritary standard deviation from (mean - potentially fatal bmi)
    if bmi > 35:
        agent.obese = True
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

            if cfr < 0.05 or (cfr < 0.11 and agent.obese == True): #5% of cases will die or if agent is obese 11% will die
                agent.model.deaths += 1
                agent.dead = True
                removeAgentFromModel(agent)
            else:
                agent.model.immune += 1
                agent.immune = True
