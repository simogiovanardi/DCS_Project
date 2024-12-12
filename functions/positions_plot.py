import matplotlib.pyplot as plt
import time




# Function to initialize the plot
def initialize_plot():
    """Initializes the plot and returns the figure, axes, and artists for agents."""
    xlim=(-10, 10) 
    ylim=(-10, 10)
    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title("Agent Trajectory")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    plt.show()
    
    # Create a dictionary to store scatter plot objects for each agent
    agents = {}
    
    return fig, ax, agents

# Function to get the marker style and color for each agent type
def get_agent_style(agent_type):
    """Returns the marker style and color for the given agent type."""
    styles = {
        'Drone': {'marker': 'X', 'color': 'blue'},
        'Vessel': {'marker': '^', 'color': 'green'},
        'Mother boat': {'marker': 's', 'color': 'red'},
    }
    return styles.get(agent_type, {'marker': 'x', 'color': 'black'})  # Default is black 'x'


def update_plot(agents_positions, ax, artists, agent_types):
    """
    :param agents_positions: Dictionary of agent names and their (x, y) positions.
    :param ax: Axes object of the plot.
    :param artists: Dictionary to track scatter plot objects for each agent.
    :param agent_types: Dictionary of agent types (e.g., 'drone', 'vessel').
    """
    for agent, position in agents_positions.items():
        # Get the agent type (drone, vessel, etc.)
        agent_type = agent_types.get(agent, 'unknown')  # Default type is 'unknown'
        
        # Get the marker style and color for this agent type
        style = get_agent_style(agent_type)
        
        if agent in artists:
            # Update the position of the existing agent
            artists[agent].set_offsets([position])
        else:
            # Add a new scatter plot for a new agent with the correct marker and color
            artists[agent] = ax.scatter(*position, label=agent, marker=style['marker'], color=style['color'])
    
    # Refresh the legend if new agents were added
    ax.legend()
    
    # Redraw the plot
    plt.draw()





