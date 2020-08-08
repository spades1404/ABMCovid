import statistics

def Rrate(model):
    if model.agents == []:
        return 0
    else:
        rvalues = [i.reproductionRate for i in model.agents if i.infected == True] #Only including if its true
        try:
            return(statistics.mean(rvalues))
        except:
            return(0)
