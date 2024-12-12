import matplotlib.pyplot as plt

def initialize_plot():
    """Initializes the plot and returns the figure, axes, and artists for agents."""
    xlim=(-10, 10)
    ylim=(-10, 10)
    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title("Drone Formation Trajectory")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    plt.show()
    
    # Create a dictionary to store scatter plot objects for each agent
    agents = {}
    
    return fig, ax, agents

def get_agent_style(agent_type):
    styles = {
        'Drone': {'marker': 'X', 'color': 'blue'},
        'Vessel': {'marker': '^', 'color': 'green'},
        'Mother boat': {'marker': 's', 'color': 'red'},
    }
    return styles.get(agent_type, {'marker': 'x', 'color': 'black'})  # Default is black 'x'

def update_plot(agents_positions, ax, artists, agent_types):
    ax.clear()
    ax.set_xlim(-10, 20)
    ax.set_ylim(-10, 20)
    ax.set_title("Drone Formation Trajectory")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    
    for agent, position in agents_positions.items():
        agent_type = agent_types.get(agent, 'unknown')
        style = get_agent_style(agent_type)
        ax.scatter(position[0], position[1], label=agent, marker=style['marker'], color=style['color'])
    
    ax.legend(loc='upper right')
    plt.draw()