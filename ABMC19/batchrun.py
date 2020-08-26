from ABMC19.Libs.Mesa.batchrunner import BatchRunner
from ABMC19.Model.model import covidModel
from ABMC19.Model.DataCollectors.collectors import *
import matplotlib.pyplot as plt
import pandas
import openpyxl

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
        "Reproduction Rate": Rrate,
        "dtl" : returndtl,
        "citl" : returncitl,
        "itl" : returnitl
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
    runData.to_excel("output.xlsx")



    return runData


batchRun(
    100,1,1,1,1,1,True,False,range(100,1050,50)
)


def listAverager(lol):
    length = len(lol[0])
    x = []
    for i in range(length):
        f = []
        for k in lol:
            f.append(k[i])

        z = 0
        for j in f:
            z+=j

        z /= len(f)
        x.append(z)

    return x



