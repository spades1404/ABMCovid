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
        outcome = random.random()

        #alter p value rather than rng
        if primaryAgent.distanced == True:
            outcome -= 0.1 #reduces the chance of infection by 10%

        elif primaryAgent.hygenic == True:
            outcome -= 0.1

        elif primaryAgent.mask == True:
            outcome -= 0.1

        elif secondaryAgent.distanced == True:
            outcome -= 0.1

        elif secondaryAgent.hygenic == True:
            outcome -= 0.1

        elif secondaryAgent.mask == True:
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


