import matplotlib.pyplot as plt
import time


def x_y_positions_plot(name, x_position, y_position):
    # Plot the current position and target

    ''' 
    plt.scatter(x_position, y_position, color="blue", label = name, marker = 'X')
    plt.title("Agent")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True)
    plt.legend()
    # Set fixed axis limits
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.pause(0.05)  # Pause for live plot update
    plt.show()
    '''

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Set plot limits (adjust to match your data range)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    # Initialize the scatter plot
    point, = ax.plot([], [], 'X', color='blue')  # Single point

    point.set_data(x_position, y_position)

    # Redraw the plot
    plt.draw()
    plt.pause(0.5)  # Pause to simulate motion (adjust duration as needed)

    # Keep the final plot visible
    plt.show()


