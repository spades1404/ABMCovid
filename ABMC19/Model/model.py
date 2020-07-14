from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

from ABMC19.Agents.agent import *
from ABMC19.Model.coordinateScripts.generateSpecialAreas import *



class covidModel(Model):

    def __init__(self, numAgents,gridWidth,gridHeight):

        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

        self.numAgents = numAgents
        self.schedule = RandomActivation(self) #Creating Scheduler
        self.grid = MultiGrid(gridWidth,gridHeight,torus=True) #Creating the Grid


        #trackers
        self.deaths = 0
        self.infected = 0
        self.cured = 0
        self.immune = 0

        #here i am generating home and work coords
        #there are many improvements that could be made later on

        allSpecialCoords = generateSpecialCoordinates(self)

        #Generating Agents

        for i in range(numAgents):
            coordSet = allSpecialCoords[i] # a dual coordinate pair which acts as the agents home and work
            a = covAgent(i,self,coordSet[0],coordSet[1])
            #im going to say all the agents begin at their home coord
            self.grid.place_agent(a,coordSet[0])

    def step(self):
        self.schedule.step()






