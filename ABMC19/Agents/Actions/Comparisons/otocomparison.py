import random

### ONE TO ONE COMPARISONS ###


def onetoonecomparison(primaryAgent,secondaryAgent):
    if secondaryAgent.infected == False or secondaryAgent.pos == secondaryAgent.homeCoord or primaryAgent.infected == True: #if they are not infected or in their home
        return

    #going to say its a coinflip wheter they are infected or not, can be changed
    outcome = random.uniform(0,1)
    if secondaryAgent.cleanly == True:
        outcome -= 0.50 # If the agent is hygienic they less likely to become infected by %

    if primaryAgent.distanced == True:
        outcome -= 0.65 # lets say being distanced reduces chances by %

    if outcome > 0.2 and primaryAgent.immune == False: # base of 80% are infected
        primaryAgent.infected = True
        primaryAgent.progression = 1
        primaryAgent.model.infected += 1

