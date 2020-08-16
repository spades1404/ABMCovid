from mesa.visualization.UserParam import UserSettableParameter

from ABMC19.Libs.Mesa.visualization.modules.CanvasGridVisualization import CanvasGrid
from ABMC19.Model.model import *
from ABMC19.Libs.Mesa.visualization.ModularVisualization import ModularServer
from ABMC19.Libs.Mesa.visualization.modules import ChartModule, TextElement

from ABMC19.Model.SpecialCoords.misc import Misc
from ABMC19.Model.SpecialCoords.hospital import Hospital
from ABMC19.Model.SpecialCoords.home import Home
from ABMC19.Model.SpecialCoords.shops import Shop
from ABMC19.Model.SpecialCoords.businesses import Business


class MyTextElement(TextElement):
    def __init__(self, model):
        self.model = model
    def render(self,model):
        rval = Rrate(model)
        text_r = "{:.2f}".format(rval)
        return f"R Value: {text_r}"

class staticTextElement(TextElement):
    def __init__(self,model):
        self.model = model
        return
    def render(self,model):
        return('''
        Buildings => Squares\n
        Agents => Circles\n
        
        Buildings:\n
        ORANGE > Homes\n
        CYAN > Hospitals\n
        YELLOW > Shops\n
        GREEN > Business (other than shops and misc areas)\n
        LIGHT PINK > Misc Areas (Mainly leisure - gyms, unessential shops etc)\n
        
        Agents:\n
        TURQOISE > Normal\n
        RED > Infected\n
        VIOLET > Immune\n
        *DEAD AGENTS ARE REMOVED FROM MODEL*\n
        ''')


def agentPortrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled" : "false",
        "r" : 0.5,
        "Layer" : 1,
        "Color" : "red"
    }


    #maybe a switch statment here?
    if agent.infected == False and agent.dead == False and agent.immune == False:
        portrayal["Color"] = "#00998F" # turqoise
    elif agent.infected == True and agent.dead == False and agent.immune == False:
        portrayal["Color"] = "#FF0010" # bright red
    elif agent.dead == True:
        return
    elif agent.immune == True and agent.dead == False and agent.infected == False:
        portrayal["Color"] = "#740AFF" # violet

    return portrayal

def cellPortrayal(building):
    portrayal = {
        "Shape": "rect", #square doesnt seem to work
        "Filled": "true",
        "w": 0.9,
        "h": 0.9,
        "Layer": 1,
        "Color" : "green"
    }
    if type(building) == Misc:
        portrayal["Color"] = "#FFA8BB"
    elif type(building) == Home:
        portrayal["Color"] = "orange"
    elif type(building) == Hospital:
        portrayal["Color"] = "cyan"
    elif type(building) == Shop:
        portrayal["Color"] = "yellow"
    elif type(building) == Business:
        portrayal["Color"] = "green"

    return portrayal


def chart(dataDicts): #takes a list of dictionaries so it can display more than one line
    return ChartModule(
        [i for i in dataDicts],
        data_collector_name= "datacollector"
    )

def startVisuals(widthHeight = 100,
                 numAgents = 40,
                 numStartInfected = 2):

    grid =  CanvasGrid(agentPortrayal,cellPortrayal,widthHeight,widthHeight,600,600)



    model_params = {
        "widthAndHeight" : widthHeight,
        "numAgents": UserSettableParameter(
            "slider",
            "Number of agents",
            widthHeight,  # Default value
            10,  # Lowest value
            1000,  # Highest value
            1,  # Increment by
            description="Choose how many agents to include in the model",
        ),
      
        "startingInfected": UserSettableParameter(
            "slider",
            "Number of agents infected at start",
            2,  # Default value
            0,  # Lowest value
            50,  # Highest value
            1,  # Increment by
            description="Choose infected agents at start",
        ),

        "chanceMask": UserSettableParameter(
            "slider",
            "Mask percentage",
            0.5,  # Default value
            0,  # Lowest value
            1,  # Highest value
            0.1,  # Increment by
            description="Choose masked agents at start",
        ),

        "chanceDistanced": UserSettableParameter(
            "slider",
            "Distanced percentage",
            0.5,  # Default value
            0,  # Lowest value
            1,  # Highest value
            0.1,  # Increment by
            description="Choose distanced agents at start",
        ),

        "chanceEssentialMovement": UserSettableParameter(
            "slider",
            "Essential movement percentage",
            0.5,  # Default value
            0,  # Lowest value
            1,  # Highest value
            0.1,  # Increment by
            description="Choose essential moving agents at start",
        ),

        "chanceHygenic": UserSettableParameter(
            "slider",
            "Hygenic percentage",
            0.5,  # Default value
            0,  # Lowest value
            1,  # Highest value
            0.1,  # Increment by
            description="Choose hygenic agents at start",
        ),
        "contactTracing" : UserSettableParameter(
            "checkbox",
            "Contact Tracing",
            False,
        ),
        "lockdown" : UserSettableParameter(
            "checkbox",
            "Lockdown",
            False
        ),
        "lockdownThreshold" : UserSettableParameter(
            "slider",
            "Lockdown Activation Threshold",
            35,
            0,
            100,
            1,
            "The threshold of infected agents at which lockdown is activated if above and deactiveated if below"
        ),
        "lockdownSafetyDayThreshold" : UserSettableParameter(
            "slider",
            "Lockdown Deactivation Tick Limit",
            40,
            40,
            300,
            1,
            "The number of ticks that the current infected agents has to be below for lockdown to be lifted"
        )
    }

    server = ModularServer(
        covidModel,
        [
            grid,
            MyTextElement(covidModel),
            chart([{"Label": "Current Infected", "Color": "Red"}]),
            chart([{"Label": "Deaths", "Color": "Black"},{"Label": "Immune", "Color": "Purple"}]),
            #staticTextElement(covidModel) This element doesnt work - try find a way to do it
        ],
        "Covid Model",
        model_params
    )

    server.port = 8521
    server.launch()

#startVisuals(50,50,20,1)