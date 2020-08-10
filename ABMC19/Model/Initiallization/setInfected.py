def setInfecteed(model):
    for i in model.agents:
        if model.agents.index(i) < model.currentInfected:
            i.infected = True
            i.carrier = True
            i.progression = 1
