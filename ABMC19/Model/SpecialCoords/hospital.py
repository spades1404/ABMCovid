from ABMC19.Model.SpecialCoords.areaofinterest import *

class Hospital(aoi):
    def __init__(self,model):
        super(Hospital, self).__init__(capacity=200,model=model)
        self.occupants = [] #tracks who is in hospital #not sure if neccessary

    def admit(self,agent):
        self.currentCapacity -= 1
        self.occupants.append(agent)

    def release(self,agent):
        self.currentCapacity -= 1
        self.occupants.remove(agent)
