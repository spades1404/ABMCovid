from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from ABMC19.Model.model import *

def agentPortrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled" : "true",
        "r" : 0.5,
        "Layer" : 1
    }

    #maybe a switch statment here?
    if agent.infected == False:
        portrayal["Color"] = "green"
    elif agent.infected == True and agent.dead == False and agent.immune == False:
        portrayal["Color"] = "red"
    #elif agent.infected == True and agent.dead == False and agent.progression == 2:
    #    portrayal["Color"] = "red"
    elif agent.dead == True:
        return
    elif agent.immune == True:
        portrayal["Color"] = "purple"

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
    grid =  CanvasGrid(agentPortrayal,width,height,500,500)

    server = ModularServer(
        covidModel,
        [
            grid,
            chart("Deaths","Black"),
            chart("Infected","Red"),
            chart("Immune","Purple")
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

#startVisuals(20,20,10,10)