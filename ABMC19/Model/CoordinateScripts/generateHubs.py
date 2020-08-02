from ABMC19.Model.SpecialCoords.gym import Gym
from ABMC19.Model.SpecialCoords.hospital import Hospital
from ABMC19.Model.SpecialCoords.shops import Shop
from ABMC19.Model.SpecialCoords.workplaces import Workplace
def generateHubs(model):

    numAgents = model.numAgents

    numHospitals = round((0.0028*numAgents)/100)
    numGyms = round((0.0001*numAgents)/100)
    numShops = round((0.0001*numAgents)/150)

    if numHospitals == 0: numHospitals = 1
    if numGyms == 0: numGyms = 1
    if numShops == 0: numShops = 1

    '''
    Assumptions
    Hospitals = 200ppl max
    Gyms = 100 ppl max 
    Shops = 150 ppl max
    '''

    shops = [Shop(model) for i in range(numShops)]
    gyms = [Gym(model) for i in range(numGyms)]
    hospitals = [Hospital(model) for i in range(numHospitals)]

    numWorkplaces = round((numAgents * 0.4 * 0.8)) - len(shops) - len(gyms) - len(hospitals) # 0.4 is the ratio of business employed ppl in uk
    if numWorkplaces == 0:
        numWorkplaces = 1

    workplaces = [Workplace(model) for i in range(numWorkplaces)]

    model.workplaces = model.workplaces + shops + gyms + hospitals + workplaces


    model.allSpecialAreas = {
        "shops":shops,
        "gyms":gyms,
        "hospitals":hospitals,
        "workplaces":workplaces,
        "houses": []
    }


    return
