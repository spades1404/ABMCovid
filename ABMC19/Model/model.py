from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from ABMC19.Agents.agent import *
from ABMC19.Model.CoordinateScripts.generateSpecialAreas import *
from ABMC19.Model.Initiallization.initAgents import generateAgents
from ABMC19.Model.CoordinateScripts.generateHubs import generateHubs
from ABMC19.Model.DataCollectors.Rrate import Rrate
from ABMC19.Model.CoordinateScripts.updateDirtyCells import updateDirtyCells


class covidModel(Model):

    def __init__(self,
                 gridWidth,
                 gridHeight,
                 numAgents,
                 startingInfected=2,
                 chanceDistanced = 0.5,
                 chanceHygenic = 0.5,
                 chanceEssentialMovement = 0.5,
                 chanceMask = 0.5
                 ):

        super(covidModel, self).__init__()
        self.gridWidth = gridWidth #model grid width
        self.gridHeight = gridHeight #model grid height

        self.numAgents = numAgents #models number of agents
        self.schedule = RandomActivation(self) #Creating Scheduler
        self.grid = MultiGrid(gridWidth,gridHeight,torus=True) #Creating the Grid

        ##############Agent P Values#################

        self.chanceDistanced = chanceDistanced
        self.chanceHygenic = chanceHygenic
        self.chanceEssentialMovement = chanceEssentialMovement
        self.chanceMask = chanceMask


        #trackers
        self.deaths = 0 #will show total deaths
        self.currentInfected = startingInfected #will show number of infected agents for one tick
        self.immune = 0 #will show total immune ppl

        #For visualisation
        self.running = True


        #here i am generating home and work coords
        #there are many improvements that could be made later on

        self.agents = [] #contains all agent objs
        self.workplaces = [] #contains all workplace objs
        self.allSpecialAreas = {} #contains all building/hub objs as a dict
        self.fullCoords = [] #Tracks coordinates that have buildings


        generateHubs(self) #the all one just includes houses too

        generateAgents(self) ##Generates all the agents for us aswell as their housing


        self.dirtyCells = [] #This will track cells that have been left infected by people who are carriers or are infected if they are





        #For data collector
        self.datacollector = DataCollector(
            model_reporters={
                "Deaths" : "deaths", #tracks total deaths
                "CurrentInfected" : "currentInfected", #tracks current tick infections
                "Immune" : "immune", #tracks total immune
                "Reproduction Rate" : Rrate(self)
            }
        )


    def step(self):
        # if self.currentInfected == 0:  # this means there is no more chance the disease will spread
        #    self.running = False #then we will stop the visual model

        self.schedule.step() # do a step

        #self.datacollector.collect(self) # collect our data

        updateDirtyCells(self)

    def returnCellBuildings(self,x,y):
        if (x,y) not in self.fullCoords:
            return False
        else:
            for i in self.workplaces:
                if i.location == (x,y):
                    return i
            for i in self.allSpecialAreas["houses"]:
                if i.location == (x,y):
                    return i








