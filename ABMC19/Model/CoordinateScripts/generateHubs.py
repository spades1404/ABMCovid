from ABMC19.Model.SpecialCoords.misc import Misc
from ABMC19.Model.SpecialCoords.hospital import Hospital
from ABMC19.Model.SpecialCoords.shops import Shop
from ABMC19.Model.SpecialCoords.home import Home

import random

def generateHubs(model):

    numAgents = model.numAgents

    #these need to be updated to reflect accurate spawn figures
    numHospitals = round((numAgents/390)/200)
    numMisc = round((numAgents/1000)*21)
    numShops = round((0.001*numAgents)/150)
    numHouses = round(numAgents/(random.uniform(2.1,5)))

    if numHospitals == 0: numHospitals = 1
    if numMisc == 0: numMisc = 1
    if numShops == 0: numShops = 1
    if numHouses == 0: numHouses = 1


    '''
    Assumptions
    Hospitals = 200ppl max
    misc = 100 ppl max 
    Shops = 150 ppl max
    '''
    hospitals = [Hospital(model) for i in range(numHospitals)]
    shops = [Shop(model) for i in range(numShops)]
    miscs = [Misc(model) for i in range(numMisc)]
    houses = [Home(model) for i in range(numHouses)]

    model.workplaces = model.workplaces + shops + miscs + hospitals


    model.allSpecialAreas = {
        "shops":shops, #for food
        "misc":miscs, #fun
        "hospitals":hospitals,
        "houses": houses #housing
    }


    return
