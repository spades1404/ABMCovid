from ABMC19.Model.SpecialCoords.areaofinterest import *
import random

class Hospital(aoi):
    def __init__(self,model):
        super(Hospital, self).__init__(capacity=200,model=model)
        self.occupants = [] #tracks who is in hospital #not sure if neccessary

    def admit(self,agent):
        self.currentCapacity -= 1
        self.occupants.append(agent)
        agent.hospitalized = True
        agent.hospital = self

    def release(self,agent):
        self.currentCapacity -= 1
        self.occupants.remove(agent)
        agent.hospitalized = False
        agent.hospital = []
        agent.movementDir = 1

    def test(self,agent):
        agent.tested = True
        if agent.infected == False:
            agent.traced = False
            agent.movementDir = 1 #send them home

        if random.random() > 0.3: #test accuracy is 70%
            if agent.model.contactTracing == True:
                self.contactTracing(agent)
            if self.currentCapacity <= 0: #we will try find them another hospital if we cant accomodate
                for i in agent.model.allSpecialAreas["hospitals"]:
                    if i.currentCapacity > 0:
                        agent.model.grid.move_agent(agent,i.location)
                        i.admit(agent)
                        break
                #these two lines only occur if the for loop didnt find anything
                agent.isolated = True
                agent.movementDir = 1
            else:
                self.admit(agent)
        else:
            agent.misdiagnosed = True



    def contactTracing(self,agent):
        #these next few lines are a really crappy way of formatting the contacted list correctly since its all screwed up - at really large populations this will no doubt make it really slow
        x = list(filter(([]).__ne__, agent.contacted))
        contacted = []
        for i in x:
            if type(i) == list:
                for j in i:
                    contacted.append(j)
            else:
                contacted.append(i)



        for i in contacted:
            if random.random() > 0.5: #50 percent chance they ignore it
                i.movementDir = 4
                i.traced = True