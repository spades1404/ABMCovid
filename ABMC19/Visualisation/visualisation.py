#from mesa.visualization.modules import CanvasGrid #Old
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
        "Shape": "circle", #square doesnt seem to work
        "Filled": "true",
        "r": 1,
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

def startVisuals(width,height,numAgents,numStartInfected):
    grid =  CanvasGrid(agentPortrayal,cellPortrayal,width,height,500,500)

    server = ModularServer(
        covidModel,
        [
            grid
        ],
        "Covid Model",
        {
            "numAgents" : numAgents,
            "gridWidth" : width,
            "gridHeight" : height,
            "startingInfected" : numStartInfected
        }
    )

    server.port = 8521
    server.launch()

#startVisuals(50,50,20,1)