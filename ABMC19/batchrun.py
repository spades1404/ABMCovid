from ABMC19.Libs.Mesa.batchrunner import BatchRunner
from ABMC19.Model.model import covidModel
from ABMC19.Model.DataCollectors.Rrate import Rrate
def bacthRun():
    fixedParam = {
        "widthAndHeight" : 50,
        "chanceDistanced" : 0.5,
        "chanceHygenic": 0.5,
        "chanceEssentialMovement": 0.5,
        "chanceMask": 0.5,
        "startingInfected": 1
    }
    variabeParam = {
        "numAgents" : range(10,500,10)
    }

    modelReporters = {
        "Deaths": "deaths",  # tracks total deaths
        "Current Infected": "currentInfected",  # tracks current tick infections
        "Immune": "immune",  # tracks total immune
        "Reproduction Rate": Rrate
    }

    batchRun = BatchRunner(
        covidModel,
        variabeParam,
        fixedParam,
        iterations = 5,
    )

    batchRun.run_all()
    runData = batchRun.get_model_vars_dataframe()
    print(runData)

bacthRun()