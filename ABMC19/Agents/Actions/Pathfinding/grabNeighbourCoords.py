def grabNeighbouringCells(agent,mooreOn):
    cells = agent.model.grid.get_neighborhood(agent.pos,
                                              moore=mooreOn,
                                              include_center=False)
    return cells