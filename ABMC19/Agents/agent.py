from mesa import Agent
from ABMC19.Agents.Actions.Comparisons.covidComparison import covidCompare
from ABMC19.Agents.Actions.Progression.progressionCheck import selfCheck
from ABMC19.Agents.Actions.Pathfinding.pathmaster import moveAgent
class covAgent(Agent):
    def __init__(self,unique_id,model,homeCoord,workCoord,infectedOnSpawn):
        super().__init__(unique_id,model)

        #person covid status
        self.dead = False
        self.infected = False
        self.immune = False
        self.obese = False
        self.ticksSinceInfection = 0 #i will say each tick is a day, this is only activated once the agent is infected

        #disease progression
        self.progression = 0
        #0=>not infected 1=>incubation 2=>symptomatic 3=>outcome


        #Coordinates of the agents workplace and homeplace
        self.homeCoord = homeCoord
        self.workCoord = workCoord

        #A variable to track their current movement plan
        self.movementDir = 0
        #I will set 0 to be home->work and 1 to be work->home, using numbers so in the future I can add more paths

        #Here im adding a check to see if this agent is infected on spawn
        if infectedOnSpawn == True:
            self.infected = True
            self.progression = 1


    def step(self):
        #first we will do our covid spread check, probably for each person we are around. THIS will be only our outcome, since other agents will also do the same
        covidCompare(self)
        #then we will self check the progression of our disease
        selfCheck(self)
        #then we will do our pathfinding
        moveAgent(self)

        return
