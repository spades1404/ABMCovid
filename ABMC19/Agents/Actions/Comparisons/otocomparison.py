import random

### ONE TO ONE COMPARISONS ###

'''
def onetoonecomparison(primaryAgent,secondaryAgent):
    if secondaryAgent.infected == False or secondaryAgent.pos == secondaryAgent.homeCoord or primaryAgent.infected == True: #if they are not infected or in their home
        return

    #going to say its a coinflip wheter they are infected or not, can be changed
    outcome = random.uniform(0,1)
    if secondaryAgent.cleanly == True:
        outcome -= 1 # Im going to say if the other agents prevents themselves from preventing the disease then the chances of getting it is reduced 100%

    if primaryAgent.distanced == True:
        outcome -= 0.75 # lets say being distanced reduces chances by 75%

    if outcome > 0.2 and primaryAgent.immune == False:
        primaryAgent.infected = True
        primaryAgent.progression = 1
        primaryAgent.model.infected += 1
'''

def otoc(
        primaryAgent,
        secondaryAgent,
        sameLocation = False,
        hospital = False, # Assuming hospitals have higher rates of infection
        workplace = False,
        dirtyCell = False
):
    if secondaryAgent.carrier == False or primaryAgent.infected == True:
        return
    else:
        outcome = random.random()

        if primaryAgent.distanced == True:
            outcome -= 0.1 #reduces the chance of infection by 10%

        elif primaryAgent.hygenic == True:
            outcome -= 0.1

        elif primaryAgent.mask == True:
            outcome -= 0.1

        elif sameLocation == True:
            outcome += 0.1

        elif hospital == True:
            outcome += 0.1

        elif workplace == True:
            outcome += 0.1

        elif dirtyCell == True:
            outcome += 0.1

        if outcome > 0.7:
            primaryAgent.infected = True
            primaryAgent.carrier = True
            primaryAgent.model.currentInfected += 1
            primaryAgent.progression = 1
            secondaryAgent.reproductionRate += 1
            primaryAgent.numberOfTimesInfected += 1


