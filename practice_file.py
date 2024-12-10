from coppeliasim_zmqremoteapi_client import RemoteAPIClient
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

    # Wait until it's time to move to the next waypoint
    while sim.getSimulationTime() - start_time < t:
        time.sleep(0.01)  # Sleep briefly to avoid busy waiting

    # Set the object's position
    sim.setObjectPosition(object_handle, [x, y, z])

# Optionally, stop the simulation after movement is complete

sim.stopSimulation()