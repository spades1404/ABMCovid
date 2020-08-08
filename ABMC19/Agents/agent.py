from mesa import Agent
from ABMC19.Agents.Actions.Pathfinding.pathmaster import moveAgent
from ABMC19.Agents.Actions.Progression.progressionCheck import selfCheck
from ABMC19.Agents.Characteristics.characteristics import *
from ABMC19.Agents.Actions.Pathfinding.grabDestCoord import grabDestCoord
from ABMC19.Agents.Actions.trails import cellInfector
from ABMC19.Agents.Actions.Comparisons.covidComparison import covidComparison
from ABMC19.Agents.Actions.Progression.progressionCheck import selfCheckNew

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


        #A variable to track their current movement plan
        self.movementDir = 1 # As work is the starting Coord, movementDir is set so the agent is initially moving to home Coord
        #I will set 0 to be home->work and 1 to be work->home, using numbers so in the future I can add more paths

        self.currentDestCoord = ()
        grabDestCoord(self)
        '''
        New Movement Paths
        0 => Work
        1 => Home
        2 => Shopping
        3 => Gym
        4 => Hospital
        '''


        #Prevention Factors
        self.distanced = RTF(model.chanceDistanced)  # True or False if they are distancing
        self.hygenic = RTF(model.chanceHygenic)  # T OR F if they are hygenic - washing hands (covers the bulk of preventative measures)
        self.essentialMovement = RTF(model.chanceEssentialMovement) # Only goes to shop and home etc #need to change the direction changer for this to work
        self.mask = RTF(model.chanceMask)


        ###Characteristics###

        #BASIC CHARACTERISTICS#
        self.gender = RTF(0.51) #TRUE = MEN FALSE = WOMEN
        self.bmi = obesityDef()
        self.age = ageDef()
        self.bame = RTF(0.13) #True = yes false = no

        #High Risk - Extremely Vulnerable#
        self.transplant = RTF(0.000015)
        self.cancer = RTF(0.0055)
        if self.gender == False:
            self.pregnant = RTF(0.025)
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
        for i in [self.badLung,self.badHeart,self.diabetes,[True if self.bmi > 30 else False],[True if self.age > 50 else False],self.bame]:
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

        self.reproductionRate = 0 #Tracks the number of people weve infected
        self.numberOfTimesInfected = 0


        # disease progression
        self.progression = 0
        # 0=>not infected 1=>incubation/asymp 2=>symptomatic 3=>outcome

        #######################################


    def step(self):

        cellInfector(self) #Checking if we have left any reminants of the disease behind

        #first we will do our covid spread check, probably for each person we are around. THIS will be only our outcome, since other agents will also do the same
        covidComparison(self)
        #then we will self check the progression of our disease
        selfCheckNew(self) #REMINDER LATER I PLAN TO USE THIS TO DECIDE IF WE WILL MOVE
        #then we will do our pathfinding
        moveAgent(self)




        #snippet for later
        #if selfCheck(self) == True:
        #    moveAgent()

        return

