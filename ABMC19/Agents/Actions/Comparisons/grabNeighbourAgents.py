def grabNeighboursAgents(agent,mooreOn):
    #lets get nearby coordinates first
    cells = agent.model.grid.get_neighborhood(agent.pos,
                                       moore=mooreOn,
                                       include_center=False)


    #then lets transform that into a list of agents
    return [k for i in cells for k in agent.model.grid.get_cell_list_contents([i])]