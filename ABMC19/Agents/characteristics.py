import random

def obesityDef():
    bmi = random.normalvariate(27.5,7.5)
    if bmi >= 35:
        return True
    else:
        return False

#we can add more characteristic checks here (like other pre existing conditions