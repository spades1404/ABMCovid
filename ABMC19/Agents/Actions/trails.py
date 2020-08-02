import random

def cellInfector(agent):
    if agent.infected == True:
        outcome = random.random()
        if agent.hygenic == False:
            outcome += 0.15 #if not hygenic they have an increased chance of leaving behind the disease
        if agent.mask == False:
            outcome += 0.15

        if outcome > 0.7:
            agent.model.dirtyCells.append([agent.pos,0])

    if agent.carrier == True: #reduced chances if they are only a carrier
        outcome = random.random()
        if agent.hygenic == False:
            outcome += 0.075 #if not hygenic they have an increased chance of leaving behind the disease
        if agent.mask == False:
            outcome += 0.075

        if outcome > 0.75:
            agent.model.dirtyCells.append([agent.pos,0])