import statistics

def Rrate(model):
    if model.agents == []:
        return 0
    rvalues = [i.reproductionRate for i in model.agents]
    # print("RVALS", rvalues)
    # print("med", statistics.mean(rvalues))
    return statistics.mean(rvalues)