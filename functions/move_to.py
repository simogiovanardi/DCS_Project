import math

def move_to(actual_X, actual_Y, actual_Z, new_X, new_Y, new_Z, velocity):
    """
    Function to calculate waypoints and time steps from the current position to a new position for an agent.

    Parameters:
    - name (str): Name or identifier of the agent.
    - actual_X, actual_Y, actual_Z (float): Current position coordinates.
    - new_X, new_Y, new_Z (float): Destination coordinates.
    - velocity (float): Desired velocity in meters per second.
    - dt (float): Time step in seconds.

    Returns:
    - steps (list): List of tuples containing waypoints and time stamps as [ (x, y, z, t), ... ].
    """

    dt=0.05
    # Calculate the total path length using the Euclidean distance formula
    path_length = math.sqrt(
        (new_X - actual_X) ** 2 +
        (new_Y - actual_Y) ** 2 +
        (new_Z - actual_Z) ** 2
    )

    if path_length == 0:
        # If the agent is already at the destination, return the current position with time zero
        return [(round(actual_X, 2), round(actual_Y, 2), round(actual_Z, 2), 0)]

    # Calculate the total time to traverse the path at the given velocity
    total_time = path_length / velocity

    # Calculate the number of steps based on the total time and time step
    n_steps = int(total_time / dt) + 1  # Add 1 to include the destination point

    # Adjust dt to fit exactly into total_time
    dt_adjusted = total_time / n_steps

    # Calculate the increments for each coordinate per step
    x_step = (new_X - actual_X) / n_steps
    y_step = (new_Y - actual_Y) / n_steps
    z_step = (new_Z - actual_Z) / n_steps

    steps = []

    for i in range(n_steps + 1):
        x = actual_X + i * x_step
        y = actual_Y + i * y_step
        z = actual_Z + i * z_step
        t = i * dt_adjusted
        steps.append((round(x, 2), round(y, 2), round(z, 2), round(t, 3)))  # Use round(t, 3) for milliseconds precision

    return steps