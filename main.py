from agents_fleets.drones_fleet import DronesFleet
#from coppeliasim_zmqremoteapi_client import RemoteAPIClient
#from functions.positions_plot import initialize_plot, get_agent_style
import numpy as np
import matplotlib as plt

"""
updated_positions = [[5,3,5],[2,5,7],[9,7,4]]
fleet1.move_drones(updated_positions, 1)

for i in waypoints_fleet1.move_drones(updated_positions, 1)

    def path_generation(self, position):
        rows = 10, cols = 10
        for col in cols:
            for row in rows:
                for drone in self.n_drones:
"""

n_drones=5
fleet = DronesFleet(n_drones)

# Define waypoints for the centroid
cols = 10
rows = 10 
height = 2
waypoints_list = []
for col in range(cols):
    for row in range(rows):
        waypoints_list.append([col, row, height])

# print(waypoints_list)


# Define desired distances (pentagon edges)
size = 5  # Size of the matrix
desired_distance = 2
desired_distances = np.full((n_drones, n_drones), desired_distance)
np.fill_diagonal(desired_distances, 0)  # Distance to itself is zero

R = 10  # Interaction range
fleet.formation_with_waypoints(waypoints_list, desired_distances, R, learning_rate=0.05, steps_per_waypoint=5)
plt.show()


