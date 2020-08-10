def grabNeighboursAgents(agent,mooreOn=False):
    #lets get nearby coordinates first
    cells = agent.model.grid.get_neighborhood(agent.pos,
                                       moore=mooreOn,
                                       include_center=True)
    return [k for i in cells for k in agent.model.grid.get_cell_list_contents([i]) if i not in agent.model.fullCoords]

def grabNeighboursOneCell(agent):
    return agent.model.grid.get_cell_list_contents(agent.pos)