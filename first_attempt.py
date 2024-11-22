import math
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# Parameters for the circular path
radius = 5.0  # Radius of the circle
center_x, center_y = 0, 0  # Center of the circle
num_points = 36  # Number of waypoints (the more points, the smoother the path)

# Generate waypoints in a circular path
waypoints = []
for k in range(num_points):
    angle = 2 * math.pi * k / num_points
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    z = 0  # Assuming the path is on a flat plane at z=0
    waypoints.append([x, y, z])


# Assume 'bike' is the object handle for your bike model in CoppeliaSim
bike_handle = sim.getObject('/Motorbike')  # Replace with your bike's actual name


def move_to_point(bike_handle1, target_position, speed=0.1):
    # Move the bike towards the target position at a given speed
    current_position = sim.getObjectPosition(bike_handle1, -1)
    direction = [target_position[i] - current_position[i] for i in range(3)]
    distance = math.sqrt(sum([d ** 2 for d in direction]))
    if distance < 0.1:
        return True  # Reached the waypoint
    norm_direction = [d / distance for d in direction]
    move_step = [norm_direction[j] * speed for j in range(3)]
    new_position = [current_position[i] + move_step[i] for i in range(3)]
    sim.setObjectPosition(bike_handle1, -1, new_position)
    return False


# Main loop to follow the waypoints
sim.startSimulation()
for point in waypoints:
    while not move_to_point(bike_handle, point):
        pass  # Keep moving until reaching the waypoint


sim.stopSimulation()

'''

from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import random

client = RemoteAPIClient()
sim = client.getObject('sim')

# Grid dimensions
rows = 10
cols = 10

sim.startSimulation()

# Example logic: Random color generation for each cell
for row in range(1, rows+1):
    for col in range(1, cols+1):
        cell_name = f"/Map/Cell_{row}_{col}"  # Assuming cells are named this way in CoppeliaSim

        cell_handle = sim.getObject(cell_name)

        # Define color logic (random in this case)
        color = [random.random(), random.random(), random.random()]  # RGB color with values [0, 1]

        # Apply color to the cell
        sim.setShapeColor(cell_handle, None, sim.colorcomponent_ambient_diffuse, color)

        # Set the desired height (Z-axis scale factor)
        height_scale = random.random()  # This will double the height of the cube

        # Scale the cube along the Z-axis only (keep X and Y scaling factors at 1 to avoid changing them)
        # sim.scaleObject(cube_handle, 1, 1, height_scale)

sim.stopSimulation()
'''
