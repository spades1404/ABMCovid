import random

### ONE TO ONE COMPARISONS ###


def otoc(
        primaryAgent,
        secondaryAgent,
        sameLocation = False,
        hospital = False, # Assuming hospitals have higher rates of infection
        workplace = False,
        dirtyCell = False
):
    if secondaryAgent.carrier == False or primaryAgent.infected == True or primaryAgent.immune == True:
        return
    else:
        x = random.random()
        outcome = 0.5

        #alter p value rather than rng
        if primaryAgent.distanced == True:
            outcome -= 0.85 #reduces the chance of infection by 85%

        elif primaryAgent.hygenic == True:
            outcome -= 0.5

        elif primaryAgent.mask == False:
            outcome -= 0.85

        elif secondaryAgent.hygenic == True:
            outcome -= 0.2

        elif secondaryAgent.mask == True:
            outcome -= 0.85

        elif sameLocation == True:
            outcome += 0.25

        elif hospital == True:
            outcome += 0.23

        elif workplace == True:
            outcome += 0.15

        elif dirtyCell == True:
            outcome += 0.1

        if x > outcome:
            primaryAgent.infected = True
            primaryAgent.carrier = True
            primaryAgent.model.currentInfected += 1
            primaryAgent.model.totalInfected += 1
            primaryAgent.progression = 1
            secondaryAgent.reproductionRate += 1
            primaryAgent.numberOfTimesInfected += 1


