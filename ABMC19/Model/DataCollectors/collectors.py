import statistics

def Rrate(model):
    if model.agents == []:
        return 0
    else:
        rvalues = [i.reproductionRate for i in model.agents]
        try:
            return(statistics.mean(rvalues))
        except:
            return(0)

def returnDeath(model):
    return model.deaths
def returnImmune(model):
    return model.immune

def returndtl(model):
    return model.deathTimeline
def returncitl(model):
    return model.currentInfectedTimeline
def returnitl(model):
    return model.immuneTimeline
