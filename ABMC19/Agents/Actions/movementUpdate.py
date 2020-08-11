import random
import numpy

def updateMovementDir(agent):
    if agent.traced == True: #if they have been contact traced, check if they are at the hospital and test them
        f = [i for i in agent.model.allSpecialAreas["hospitals"] if agent.pos in i.location]
        if f != []:
            if agent.tested == False:
                f[0].test(agent)  # this tests the agent for covid
            return False
    if agent.progression == 2 and agent.tested == False:
        ########Check if they are at hospital (andf if they need a test)

        f = [i for i in agent.model.allSpecialAreas["hospitals"] if agent.pos in i.location]
        if f != []:
            f[0].test(agent) #this tests the agent for covid
            return False
        ##############
        if random.random() > 0.4: #60% chance that they will go to hospital on discovering symptoms
            agent.movementDir = 4
            return True

    elif agent.hospitalized == True or (agent.isolating == True and agent.pos == agent.home.location[0]):
        return False

    else:
        if agent.pos == agent.home.location[0]:
            agent.movementDir = chooseNewDir(agent) #go somewhere different if they are not home
            if agent.movementDir == 1:
                return False #tells the agent not to move
        elif agent.pos == agent.currentDestCoord:
            agent.movementDir = 1

        return True #Tells the agent to move




def chooseNewDir(agent): #We can update this later so theres higher chances of going home etc

    dataSet1 = [0.4,0,0.2,0.4] #standard movement - going work is 40% going food shop is 30% and going out for fun or other misc activities is 40% (home is 0% since its only activated when at home)
    dataSet2 = [0.4,0.4,0.2,0] #when doing essential movement only - staying at home also has a chance now
    dataSet3 = [0.45,0.45,0.1,0] #potential set for lockdown scenario


    inUseSet = []
    if agent.essentialMovement == True:
        inUseSet = dataSet2
    else:
        inUseSet = dataSet1
    while True:
        #x = random.randint(0, 4)

        x = (numpy.random.choice(numpy.arange(0,4), p = inUseSet))
        if x == agent.movementDir:
            continue
        else:
            return x
