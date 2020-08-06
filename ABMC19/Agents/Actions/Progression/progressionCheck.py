import random
from ABMC19.Agents.Actions.Progression.removeAgentFromModel import removeAgentFromModel

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
            agent.model.currentInfected -= 1
            x = bool(random.getrandbits(1)) #going to say its 50/50 that the

            cfr = random.random() #cfr is case fatality rate, im going of an avg of 5% cases result in death (however this can be alterable)


            if agent.bmi > 30:
                cfr += 0.2 #lets say it adds a 20% risk of death


            if cfr > 0.95: #5% chance of death
                agent.model.deaths += 1
                agent.dead = True
                removeAgentFromModel(agent)
            else:
                agent.model.immune += 1
                agent.immune = True

def selfCheckNew(agent):
    tsi = (agent.ticksSinceInfection) #TO CHANGE TICK TIME REPRESENTATION DIVIDE THE TSI BY A FACTOR OF 24- 1TICK=6HOOURS = DIVIDE BY 4

    if agent.infected == True:
        agent.ticksSinceInfection += 1

    if agent.progression == 1:
        dayProg = tsi #currentDay of disease
        randProgressionDate = random.normalvariate(11.5,2) #setting this as a random day in which the disease will progress
        for i in range(agent.highRisks):
                dayProg *= 1.1 #going to say that it accelerates the progression by 10% THIS CAN BE CHANGED TO ADD A DAY OR SOMETHING DIFFERENT
        for i in range(agent.moderateRisks):
                dayProg *= 1.05 #same thing but increases 5%
        #by multiplying the tsi it makes the progression exponentially worse if you have a risk factor

        if dayProg >= randProgressionDate:
            agent.progression = 2

    elif agent.progression == 2:
        dayProg = tsi  # currentDay of disease
        randProgressionDate = random.normalvariate(24,2)  # setting this as a random day in which the disease will progress
        for i in range(agent.highRisks):
                dayProg *= 1.1  # going to say that it accelerates the progression by 10% THIS CAN BE CHANGED TO ADD A DAY OR SOMETHING DIFFERENT
        for i in range(agent.moderateRisks):
                dayProg *= 1.05  # same thing but increases 5%
        # by multiplying the tsi it makes the progression exponentially worse if you have a risk factor

        if dayProg >= randProgressionDate:

            cfr = random.random()

            for i in range(agent.highRisks):
                    cfr += 0.1 #being high risk increases risk of death by 10%
            for i in range(agent.moderateRisks):
                    cfr += 0.05 #being moderate risk increases risk of death by 5%

            if agent.hospitalized == True:
                cfr -= 0.3 #being in hospital reduces chance of death by 30%



            agent.progression = 3
            agent.model.currentInfected -= 1
            agent.infected = False


            if cfr > 0.9: #10% chance of death
                agent.model.deaths += 1
                agent.dead = True
                removeAgentFromModel(agent)
            elif cfr < 0.9:

                randomChance = random.uniform(0,1)

                if agent.numberOfTimesInfected > 1:
                    randomChance += 0.15

                if randomChance > 0.9: #10 percent chance of immunity
                    agent.immune = True
                    agent.model.immune += 1
                    agent.carrier = True
                else:
                    agent.progression = 0
                    agent.ticksSinceInfection = 0




