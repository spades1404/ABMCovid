#from Mesa import Agent Old

from ABMC19.Libs.Mesa import Agent

from ABMC19.Agents.Actions.Pathfinding.pathmaster import moveAgent
from ABMC19.Agents.Characteristics.characteristics import *
from ABMC19.Agents.Actions.Pathfinding.grabDestCoord import grabDestCoord
from ABMC19.Agents.Actions.infectionTrails import cellInfector
from ABMC19.Agents.Actions.Comparisons.covidComparison import covidComparison
from ABMC19.Agents.Actions.progressionCheck import diseaseProgression
from ABMC19.Agents.Actions.contactTrails import contactedAgents
from ABMC19.Agents.Actions.movementUpdate import updateMovementDir

class covAgent(Agent):
    def __init__(self,
                 unique_id,
                 model,
                 home,
                 work,
                 infectedOnSpawn = False):


        super().__init__(unique_id,model)

        #Coordinates of the agents workplace and homeplace
        self.home = home #this is a home object
        self.work = work #this is a aoi super obj


        #variables to track their current movement plan
        self.movementDir = 1 # As work is the starting Coord, movementDir is set so the agent is initially moving to home Coord

        self.currentDestCoord = ()
        grabDestCoord(self)
        '''
        New Movement Paths
        0 => Work
        1 => Home
        2 => Shopping - food shops - neccessary
        3 => Misc areas - like going gym, restaurants, etc
        4 => Hospital
        '''


        #Prevention Factors
        self.distanced = RTF(model.chanceDistanced)  # True or False if they are distancing
        self.hygenic = RTF(model.chanceHygenic)  # T OR F if they are hygenic - washing hands (covers the bulk of preventative measures)
        self.essentialMovement = RTF(model.chanceEssentialMovement) # Only goes to shop and home etc #need to change the direction changer for this to work
        self.mask = RTF(model.chanceMask)

        #For contact tracing
        self.traced = False  # Used to check if they have been contact traced
        self.contacted = []
        ###Characteristics###

        #BASIC CHARACTERISTICS#
        self.gender = RTF(0.49) #TRUE = MEN FALSE = WOMEN
        self.obese = RTF(0.287)
        self.age = ageDef()
        self.bame = RTF(0.13) #True = yes false = no

        #High Risk - Extremely Vulnerable#
        self.transplant = RTF(0.000015)
        self.cancer = RTF(0.0055)
        if self.gender == False:
            self.pregnant = RTF(0.05)
        else:
            self.pregnant = False

        self.highRisks = 0
        for i in [self.transplant,self.cancer,self.pregnant]:
            if i == True:
                self.highRisks+=1
        #Moderate Risk#

        self.badLung = RTF(0.2)
        self.badHeart = RTF(0.11)
        self.diabetes = RTF(0.0625)

        self.moderateRisks = 0
        for i in [self.badLung,self.badHeart,self.diabetes,self.obese,[True if self.age > 50 else False],self.bame]:
            if i == True:
                self.moderateRisks += 1

        #PLUS AGE AND BMI

        ############################


        #######STATUS TRACKERS########
        self.ticksSinceInfection = 0  # i will say each tick is a day, this is only activated once the agent is infected


        self.carrier = infectedOnSpawn #are they a carrier
        self.infected = infectedOnSpawn  # Are they infected
        self.dead = False  # Are they dead?
        self.immune = False  # are they immune

        self.hospitalized = False #are in hospital
        self.isolating = False #are they isolating

        ###Tests
        self.misdiagnosed = False
        self.tested = False
        ###

        self.hospital = [] #used to store which hospital they are in if they get admitted

        self.reproductionRate = 0 #Tracks the number of people weve infected
        self.numberOfTimesInfected = 0


        # disease progression
        self.progression = 0
        # 0=>not infected 1=>incubation/asymp 2=>symptomatic 3=>outcome

        #######################################


    def step(self):
        if self.infected == False:
            covidComparison(self)  # comparisons with nearby agents to see if weve caught the disease
        else:
            contactedAgents(self) #adds contacted agents if we are infected
            cellInfector(self) #Checking if we have left any reminants of the disease behind
            diseaseProgression(self)#then we will self check the progression of our disease

        if updateMovementDir(self) == True: #this func will tell us if we should move
            moveAgent(self)


        return

