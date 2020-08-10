def grabNeighbouringCells(agent,
                          mooreOn,
                          center = False):

    cells = agent.model.grid.get_neighborhood(agent.pos,
                                              moore=mooreOn,
                                              include_center=center)
    return cells