import statistics

def Rrate(model):
    if model.agents == []:
        return 0
    else:
        rvalues = [i.reproductionRate for i in model.agents]
        return(statistics.mean(rvalues))