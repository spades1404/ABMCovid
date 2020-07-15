import random

def onetoonecomparison(primaryAgent,secondaryAgent):
    if secondaryAgent.infected == False or secondaryAgent.pos == secondaryAgent.homeCoords: #if they are not infected or in their home
        return

    #going to say its a coinflip wheter they are infected or not, can be changed
    outcome = random.uniform(0,1)

    if outcome > 0.5 and primaryAgent.immune == False:
        primaryAgent.infected = True
        primaryAgent.model.infected += 1

