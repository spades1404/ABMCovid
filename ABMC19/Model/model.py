from ABMC19.Libs.Mesa import Model
from ABMC19.Libs.Mesa.time import RandomActivation
from ABMC19.Libs.Mesa.space import MultiGrid
from ABMC19.Libs.Mesa.datacollection import DataCollector

from ABMC19.Agents.agent import *
from ABMC19.Model.CoordinateScripts.generateSpecialAreas import *


from ABMC19.Model.Initiallization.initAgents import generateAgents
from ABMC19.Model.Initiallization.setInfected import setInfecteed
from ABMC19.Model.CoordinateScripts.generateHubs import generateHubs
from ABMC19.Model.DataCollectors.Rrate import Rrate
from ABMC19.Model.CoordinateScripts.updateDirtyCells import updateDirtyCells


class covidModel(Model):

    def __init__(self,
                 widthAndHeight,
                 numAgents,
                 startingInfected=2,
                 chanceDistanced = 0.5,
                 chanceHygenic = 0.5,
                 chanceEssentialMovement = 0.5,
                 chanceMask = 0.5,
                 contactTracing = False, #contact tracing is experimental
                 lockdown = True, ##lockdown in threshholds
                 lockdownThreshold = 40, #the threshold for activating lockdown
                 lockdownSafetyDayThreshold = 50, #number of days that the threshhold must be below the threshold for lockdown to be lifted
                 ):

        super(covidModel, self).__init__()
        self.gridWidth = widthAndHeight #model grid width
        self.gridHeight = widthAndHeight #model grid height

        self.numAgents = numAgents #models number of agents
        self.schedule = RandomActivation(self) #Creating Scheduler
        self.grid = MultiGrid(widthAndHeight,widthAndHeight,torus=True) #Creating the Grid

        self.contactTracingOn = contactTracing
        self.lockdownOn = lockdown
        self.inLockdown = False
        self.lockdownThreshold = lockdownThreshold
        self.lockdownDayLift = lockdownSafetyDayThreshold
        #self.fastTest = fastTest #going to add very fast testing in the future

        ##############Agent P Values#################

        self.chanceDistanced = chanceDistanced
        self.chanceHygenic = chanceHygenic
        self.chanceEssentialMovement = chanceEssentialMovement
        self.chanceMask = chanceMask


        #trackers
        self.deaths = 0 #will show total deaths
        self.currentInfected = startingInfected #will show number of infected agents for one tick
        self.immune = 0 #will show total immune ppl
        self.knownInfected = 0 #this tracks the known infected by the models authorities - since you only know if someone is infected after testing them

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

        setInfecteed(self)




        self.dirtyCells = [] #This will track cells that have been left infected by people who are carriers or are infected if they are





        #For data collector
        self.datacollector = DataCollector(
            model_reporters={
                "Deaths" : "deaths", #tracks total deaths
                "Current Infected" : "currentInfected", #tracks current tick infections
                "Immune" : "immune", #tracks total immune
                "Reproduction Rate" : Rrate,
                "Known Infected" : "knownInfected"
            }
        )

        print("Model Initialization Successful! - Running")

    def step(self):

        #for i in self.agents: i.reproductionRate = 0

        if self.currentInfected == 0:  # this means there is no more chance the disease will spread
            self.running = False #then we will stop the visual model

        if self.lockdownOn == True:
            self.checkLockdownStatus()

        # print("Rate", Rrate(self))
        self.schedule.step() # do a step

        self.datacollector.collect(self) # collect our data

        updateDirtyCells(self)






    def returnCellBuildings(self,x,y):

        if (x,y) not in self.fullCoords:
            return False
        else:
            for i in self.allSpecialAreas:
                for j in self.allSpecialAreas[i]:
                    if (x,y) in j.location:
                        return j

    def checkLockdownStatus(self):
        if self.currentInfected > self.lockdownThreshold:
            self.inLockdown = True
        elif [True if i < self.lockdownThreshold else False for i in (list(self.datacollector.get_model_vars_dataframe()["Current Infected"][-self.lockdownDayLift:]))] == [True for i in range(self.lockdownDayLift)]:
            self.inLockdown = False

    def removeAgent(self,agent):
        self.schedule.remove(agent)










