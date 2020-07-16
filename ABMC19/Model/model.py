from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from ABMC19.Agents.agent import *
from ABMC19.Model.coordinateScripts.generateSpecialAreas import *



class covidModel(Model):

    def __init__(self,gridWidth,gridHeight,numAgents,startingInfected):

        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

        self.numAgents = numAgents
        self.schedule = RandomActivation(self) #Creating Scheduler
        self.grid = MultiGrid(gridWidth,gridHeight,torus=True) #Creating the Grid


        #trackers
        self.deaths = 0 #will show total deaths
        self.infected = startingInfected #will show number of infected agents for one tick
        # self.cured = 0 #this will only matter if the immunity is random
        self.immune = 0 #will show total immune ppl

        #For visualisation
        self.running = True


        #For data collector
        self.datacollector = DataCollector(
            model_reporters={
                "Deaths" : "deaths",
                "Infected" : "infected",
                "Immune" : "immune"
            }
        )

        #here i am generating home and work coords
        #there are many improvements that could be made later on

        allSpecialCoords = generateSpecialCoordinates(self)

        #Generating Agents

        for i in range(numAgents):

            #rudimentary way to do the starting num of infected agents
            if i <startingInfected :
                infectedAgent = True

            else:
                infectedAgent = False

            coordSet = allSpecialCoords[i] # a dual coordinate pair which acts as the agents home and work
            a = covAgent(i,self,coordSet[0],coordSet[1],infectedAgent)
            #im going to say all the agents begin at their home coord
            self.grid.place_agent(a,coordSet[0])

            self.schedule.add(a)




    def step(self):
        self.schedule.step()

        self.datacollector.collect(self)

        if self.infected == 0:  # this means there is no more chance the disease will spread
            self.running = False #then we will stop the visual model








