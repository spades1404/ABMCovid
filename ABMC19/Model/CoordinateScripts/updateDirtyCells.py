def updateDirtyCells(model):
    for i in model.dirtyCells:
        i[1] += 1
        if i[1] == 2:
            model.dirtyCells.remove(i)
