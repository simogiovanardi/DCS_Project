"""from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from functions.move_to import move_to
import time

client = RemoteAPIClient()
sim = client.getObject('sim')

object_handle = sim.getObject('/Drone1')

current_position = (0, 0, 1)
actual_X, actual_Y, actual_Z = current_position

new_X = 2.0  # Replace with your target X
new_Y = 2.0  # Replace with your target Y
new_Z = actual_Z  # Keep the same Z if moving in 2D plane
velocity = 0.5    # Meters per second
dt = 0.05         # Time step in seconds

waypoints = move_to(actual_X, actual_Y, actual_Z, new_X, new_Y, new_Z, velocity)



sim.startSimulation()

sim.setObjectPosition(object_handle, current_position)

start_time = sim.getSimulationTime()

for waypoint in waypoints:
    x, y, z, t = waypoint
print(list + (i*0.1) for i in range(5))
    # Wait until it's time to move to the next waypoint
    while sim.getSimulationTime() - start_time < t:
        time.sleep(0.01)  # Sleep briefly to avoid busy waiting

    # Set the object's position
    sim.setObjectPosition(object_handle, [x, y, z])

# Optionally, stop the simulation after movement is complete

sim.stopSimulation()"""

"""list = [1,2,3]
list_2 = list.copy()
for i in range(len(list_2)):
    list_2[i] = list_2[i] +1

print(list)
print(list_2)
# print(list + (i*0.1) for i in range(5))


spawning_position = [-2, 2, 0]

new_spawn_positions = [spawning_position[j]+(0.1*i) for i in range(5) for j in range(len(spawning_position))]
print(new_spawn_positions)
"""




def generate_zigzag(rows, cols):
    zigzag_path = []
    for col in range(cols):
        if col % 2 == 0:  # Even column: top-to-bottom
            for row in range(rows):
                zigzag_path.append([row, col])
        else:  # Odd column: bottom-to-top
            for row in range(rows - 1, -1, -1):
                zigzag_path.append([row, col])
    return zigzag_path

# Parameters
rows = 10
cols = 10

# Generate the zigzag path
zigzag_points = generate_zigzag(rows, cols)

# Print the zigzag path
print("Zigzag Path:")
for point in zigzag_points:
    print(point)