import statistics

def Rrate(model):
    if model.agents == []:
        return 0
    rvalues = [i.reproductionRate for i in model.agents]
    return(statistics.median(rvalues))