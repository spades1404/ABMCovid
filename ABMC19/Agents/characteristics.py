import random

def obesityDef():
    bmi = random.normalvariate(27.5,7.5)
    if bmi >= 35:
        return True
    else:
        return False

def hygieneDef():
    if random.random() < 0.6: # Arbritary number of people wear a mask when going out / handwash regularly (60%)
        return True
    else:
        return False

def distanceDef():
    if random.random() < 0.3:  # Some percentage of people obey social distancing (30%)
        return True
    else:
        return False

#we can add more characteristic checks here (like other pre existing conditions