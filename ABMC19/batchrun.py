from ABMC19.Libs.Mesa.batchrunner import BatchRunner
from ABMC19.Model.model import covidModel
from ABMC19.Model.DataCollectors.collectors import *
import matplotlib.pyplot as plt
def batchRun(
        grid,
        dist,
        hyg,
        ess,
        mask,
        sinf,
        con,
        lock,
        numa #must be range obj range(10,500,10)
):
    fixedParam = {
        "widthAndHeight" : grid,
        "chanceDistanced" : dist,
        "chanceHygenic": hyg,
        "chanceEssentialMovement": ess,
        "chanceMask": mask,
        "startingInfected": sinf,
        "contactTracing" : con,
        "lockdown" : lock
    }
    variabeParam = {
        "numAgents" : numa
    }

    modelReporters = {
        "Deaths": returnDeath,  # tracks total deaths
        "Immune": returnImmune,  # tracks total immune
        "Reproduction Rate": Rrate
    }

    batchRun = BatchRunner(
        covidModel,
        variabeParam,
        fixedParam,
        iterations = 5,
        model_reporters=modelReporters
    )

    batchRun.run_all()
    runData = batchRun.get_model_vars_dataframe()
    runData.head()
    print(runData.columns)
    print(runData)
    #plt.scatter(runData["Run"],runData["Reproduction Rate"])
    plt.subplot(1,2,1)
    plt.scatter(runData["numAgents"],runData["Deaths"])
    plt.title("Deaths")
    plt.subplot(1,2,2)
    plt.scatter(runData["numAgents"],runData["Immune"])
    plt.title("Immune")

    #plt.plot(runData["Run"], runData["Immune"])

    plt.show()




    return runData

#batchRun(
#    20,1,1,1,1,1,False,False,range(10,100,10)
#)
