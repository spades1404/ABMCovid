from mesa.visualization.UserParam import UserSettableParameter


from ABMC19.Model.model import *

from ABMC19.Libs.Mesa.visualization.modules.CanvasGridVisualization import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement

from ABMC19.Model.SpecialCoords.misc import Misc
from ABMC19.Model.SpecialCoords.hospital import Hospital
from ABMC19.Model.SpecialCoords.home import Home
from ABMC19.Model.SpecialCoords.shops import Shop


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
        "key": UserSettableParameter(
            "static_text",
            value=
            '''
            <h4>Buildings: Squares</h1>
            <p style="font-size:16px;">
              <span style="color: orange">Homes</span><br> 
              <span style="color: #F2C800">Shops</span><br>
              <span style="color: #00D6D6">Hospitals</span><br>
              <span style="color: #F19CBB">Misc Areas (libraries, gyms, etc.)</span> 
            </p>

            <h4>Agents: Circles</h1>
            <p style="font-size:16px;" >
              <span style="color: #00998F">Susceptible</span><br> 
              <span style="color: #FF0010">Infected</span><br>
              <span style="color: #740AFF">Immune</span><br>
              Dead (removed from the model)
            </p>
            '''
        ),
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
            1000,
            10,
            "The threshold of infected agents at which lockdown is activated if above and deactiveated if below"
        ),
        "lockdownSafetyDayThreshold" : UserSettableParameter(
            "slider",
            "Lockdown Deactivation Tick Limit",
            500,
            250,
            1500,
            50,
            "The number of ticks that the current infected agents has to be below for lockdown to be lifted"
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

startVisuals()