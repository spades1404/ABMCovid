from mesa.visualization.UserParam import UserSettableParameter

from ABMC19.ModifiedMesa.mesa.visualization.modules.CanvasGridVisualization import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement
from ABMC19.Model.model import *

from ABMC19.Model.SpecialCoords.gym import Gym
from ABMC19.Model.SpecialCoords.hospital import Hospital
from ABMC19.Model.SpecialCoords.home import Home
from ABMC19.Model.SpecialCoords.shops import Shop
from ABMC19.Model.SpecialCoords.workplaces import Workplace


class MyTextElement(TextElement):
    def __init__(self, model):
        self.model = model
    def render(self,model):
        rval = Rrate(model)
        text_r = "{:.2f}".format(rval)
        return f"R Value: {text_r}"

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
        portrayal["Color"] = "gold"
    elif agent.infected == False and agent.dead == False and agent.immune == False:
        portrayal["Color"] = "red"
    #elif agent.infected == True and agent.dead == False and agent.progression == 2:
    #    portrayal["Color"] = "red"
    elif agent.dead == True:
        return
    elif agent.immune == True:
        portrayal["Color"] = "purple"

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
    if type(building) == Gym:
        portrayal["w"] = "2.8"
        portrayal["h"] = "2.8"
        portrayal["Color"] = "purple"
    elif type(building) == Home:
        portrayal["Color"] = "orange"
    elif type(building) == Hospital:
        portrayal["Color"] = "cyan"
        portrayal["w"] = "2.8"
        portrayal["h"] = "2.8"
    elif type(building) == Shop:
        portrayal["w"] = "2.8"
        portrayal["h"] = "2.8"
        portrayal["Color"] = "yellow"
    elif type(building) == Workplace:
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
    }

    server = ModularServer(
        covidModel,
        [
            grid,
            MyTextElement(covidModel),
            chart([{"Label": "Current Infected", "Color": "Red"}]),
            chart([{"Label": "Deaths", "Color": "Black"},{"Label": "Immune", "Color": "Purple"}]),
        ],
        "Covid Model",
        model_params
    )

    server.port = 8521
    server.launch()

#startVisuals(50,50,20,1)