import random

def obesityDef():
    bmi = random.normalvariate(27.5,7.5)
    if bmi >= 35:
        return True
    else:
        return False

def hygieneDef():
    if random.random() < 0.6: # Percentage of people wear a mask/handwash regularly
        return True
    else:
        return False

def distanceDef():
    if random.random() < 0.43:  # Percentage of people obey social distancing
        return True
    else:
        return False

def hubDef():
    if random.random() < 0.81:   # Percentage of people going to work instead of a hub
        return 0    # Movement home->work
    else:
        return 2    # Movement home->hub

def reinfectDef():
    if random.random() < 0.005: #Percentage of people getting reinfected (very low because it is unlikely)
        return True

#we can add more characteristic checks here (like other pre existing conditions)
