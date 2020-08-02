import random

def updateMovementDirection(agent):
    if agent.pos == agent.work.location:
        agent.movementDir = chooseNewDir(0)
    elif agent.pos == agent.home.location:
        agent.movementDir = chooseNewDir(1)
    elif agent.pos in [i.location for i in agent.model.allSpecialAreas["shops"]]:
        agent.movementDir = 1
    elif agent.pos in [i.location for i in agent.model.allSpecialAreas["gyms"]]:
        agent.movementDir =  chooseNewDir(2)
    elif agent.pos in [i.location for i in agent.model.allSpecialAreas["hospitals"]]:
        agent.movementDir =  1


def chooseNewDir(current): #We can update this later so theres higher chances of going home etc
    while True:
        x = random.randint(0, 4)
        if x == current:
            continue
        else:
            return x
