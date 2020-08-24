import random

def diseaseProgression(agent):
    tsi = (agent.ticksSinceInfection)/4 #TO CHANGE TICK TIME REPRESENTATION DIVIDE THE TSI BY A FACTOR OF 24- 1TICK=6HOOURS = DIVIDE BY 4

    if agent.infected == True:
        agent.ticksSinceInfection += 1
    else:
        return

    if agent.progression == 1:
        dayProg = tsi #currentDay of disease
        randProgressionDate = random.normalvariate(5.1,2.5) #setting this as a random day in which the disease will progress
        for i in range(agent.highRisks):
                dayProg *= 1.5 #going to say that it accelerates the progression by 50% THIS CAN BE CHANGED TO ADD A DAY OR SOMETHING DIFFERENT
        for i in range(agent.moderateRisks):
                dayProg *= 1.1 #same thing but increases 5%
        #by multiplying the tsi it makes the progression exponentially worse if you have a risk factor

        if dayProg >= randProgressionDate:
            agent.progression = 2

    elif agent.progression == 2:
        dayProg = tsi  # currentDay of disease
        randProgressionDate = random.normalvariate(21,7)  # setting this as a random day in which the disease will progress
        for i in range(agent.highRisks):
                dayProg *= 1.5  # going to say that it accelerates the progression by 10% THIS CAN BE CHANGED TO ADD A DAY OR SOMETHING DIFFERENT
        for i in range(agent.moderateRisks):
                dayProg *= 1.1  # same thing but increases 5%
        # by multiplying the tsi it makes the progression exponentially worse if you have a risk factor

        if dayProg >= randProgressionDate:

            cfr = 0.01
            x = random.random()

            for i in range(agent.highRisks):
                    cfr += 0.2 #being high risk increases risk of death by 20%
            for i in range(agent.moderateRisks):
                    cfr += 0.05 #being moderate risk increases risk of death by 5%

            if agent.hospitalized == True:
                cfr -= 0.5 #being in hospital reduces chance of death by 50%



            agent.progression = 3
            agent.model.currentInfected -= 1
            agent.infected = False
            agent.isolating = False

            agent.tested = False
            if agent.hospitalized == True:
                agent.hospitalized = False
                agent.hospital.release(agent)


            if x < cfr:
                agent.model.deaths += 1
                agent.dead = True
                agent.model.removeAgent(agent)

            else:

                randomChance = random.uniform(0,1)

                if randomChance > 0.8: #80 percent chance of immunity
                    agent.immune = True
                    agent.model.immune += 1
                    agent.carrier = True
                else:
                    agent.progression = 0
                    agent.ticksSinceInfection = 0
                    return





