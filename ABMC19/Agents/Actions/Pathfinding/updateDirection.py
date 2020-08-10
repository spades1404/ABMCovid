import random
import numpy

def updateMovementDirection(agent):
    if agent.pos == agent.work.location:
        agent.movementDir = chooseNewDir(agent)
    elif agent.pos == agent.home.location:
        agent.movementDir = chooseNewDir(agent)
    elif agent.pos in [i.location for i in agent.model.allSpecialAreas["shops"]]:
        agent.movementDir = 1
    elif agent.pos in [i.location for i in agent.model.allSpecialAreas["gyms"]]:
        agent.movementDir =  1
    elif agent.pos in [i.location for i in agent.model.allSpecialAreas["hospitals"]]:
        agent.movementDir =  1





def chooseNewDir(agent): #We can update this later so theres higher chances of going home etc

    dataSet1 = [0.3,0.3,0.25,0.15,0] #standard movement
    dataSet2 = [0.45,0.45,0.1,0,0] #when doing essential movement only

    inUseSet = []
    if agent.essentialMovement == True:
        inUseSet = dataSet2
    else:
        inUseSet = dataSet1
    while True:
        #x = random.randint(0, 4)

        x = (numpy.random.choice(numpy.arange(0,5), p = inUseSet))
        if x == agent.movementDir:
            continue
        else:
            return x
