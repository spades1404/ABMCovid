def grabNeighboursAgents(agent,mooreOn):
    #lets get nearby coordinates first
    cells = agent.model.grid.get_neighborhood(agent.pos,
                                       moore=mooreOn,
                                       include_center=False)
    return [k for i in cells for k in agent.model.grid.get_cell_list_contents([i])]

def grabNeighboursOneCell(agent):
    return agent.model.grid.get_cell_list_contents(agent.pos)