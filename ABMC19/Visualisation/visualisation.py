from mesa.visualization.UserParam import UserSettableParameter

from ABMC19.ModifiedMesa.mesa.visualization.modules.CanvasGridVisualization import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from ABMC19.Model.model import *

from ABMC19.Model.SpecialCoords.gym import Gym
from ABMC19.Model.SpecialCoords.hospital import Hospital
from ABMC19.Model.SpecialCoords.home import Home
from ABMC19.Model.SpecialCoords.shops import Shop
from ABMC19.Model.SpecialCoords.workplaces import Workplace

def agentPortrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled" : "false",
        "r" : 0.5,
        "Layer" : 1,
        "Color" : "red"
    }


    #maybe a switch statment here?
    if agent.infected == False:
        portrayal["Color"] = "gold"
    elif agent.infected == True and agent.dead == False and agent.immune == False:
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
        portrayal["Color"] = "purple"
    elif type(building) == Home:
        portrayal["Color"] = "orange"
    elif type(building) == Hospital:
        portrayal["Color"] = "cyan"
    elif type(building) == Shop:
        portrayal["Color"] = "yellow"
    elif type(building) == Workplace:
        portrayal["Color"] = "green"

    return portrayal

def chart(tracker,colour):
    return (
        ChartModule(
            [
                {
                    "Label" : tracker,
                    "Color" : colour
                }
            ],
            data_collector_name = "datacollector"
        )
    )


def USP(type,title,defV,lowV,hiV,incr,desc):
    return UserSettableParameter(
        type,
        title,
        defV,
        lowV,
        hiV,
        incr,
        desc
    )



def startVisuals(width,
                 height,
                 numAgents = 40,
                 numStartInfected = 2):

    #wh  = USP("slider","Grid Size",width,10,1000,1,"Choose the grid size x by x")
    grid =  CanvasGrid(agentPortrayal,cellPortrayal,width,height,600,600)



    model_params = {
        "numAgents": USP("slider","Number of Agents",numAgents,10,1000,1,"Choose how many agents to include in the model"),
        "startingInfected": USP("slider", "Number of agents infected at start", numStartInfected, 0, 50, 1,"Choose infected agents at start"),
        "gridWidth": width,
        "gridHeight": height,



    }

    server = ModularServer(
        covidModel,
        [
            grid,
            chart("CurrentInfected","Red"),
            chart("Deaths","Black"),
            chart("Immune","Purple"),
            chart("Reproduction Rate","Orange")
        ],
        "Covid Model",
        # {
        #     "numAgents" : numAgents,
        #     "gridWidth" : width,
        #     "gridHeight" : height,
        #     "startingInfected" : numStartInfected
        # }
        model_params
    )

    server.port = 8521
    server.launch()

#startVisuals(50,50,20,1)