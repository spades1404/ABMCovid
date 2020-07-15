def grabNeighboursAgents(agent,mooreOn):
    #lets get nearby coordinates first
    cells = agent.model.grid.get_neighborhood(agent.pos,
                                       moore=mooreOn,
                                       include_center=False)

    #then lets transform that into a list of agents
    agents = []

    for i in cells:
        agents + agent.model.grid.get_cell_list_contents([i])

    return agents