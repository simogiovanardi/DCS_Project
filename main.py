from agents_fleets.drones_fleet import DronesFleet
import numpy as np
from functions.drones_formation_path import generate_zigzag

# Number of drones
n_drones = 5

# Create the fleet
fleet = DronesFleet(n_drones)

# Define waypoints for the centroid to follow
# Define waypoints for the centroid
cols = 10
rows = 10 
height = 2
waypoints_list = generate_zigzag(rows, cols, height)

# Radius used in DronesFleet
radius = 1

# Calculate side and diagonal lengths for a pentagon
side_length = 2 * radius * np.sin(np.pi / n_drones)
diagonal_length = 2 * radius * np.sin(2 * np.pi / n_drones)

# Initialize desired distances matrix
desired_distances = np.zeros((n_drones, n_drones))

for i in range(n_drones):
    for j in range(n_drones):
        if i == j:
            desired_distances[i][j] = 0  # Zero distance to self
        elif (j == (i + 1) % n_drones) or (j == (i - 1) % n_drones):
            desired_distances[i][j] = side_length  # Adjacent drones
        else:
            desired_distances[i][j] = diagonal_length  # Non-adjacent drones

# Set the maximum interaction range slightly larger than the maximum desired distance
R = diagonal_length + 2

# Run the formation control with waypoints
fleet.formation_with_waypoints(
    waypoints_list=waypoints_list,
    desired_distances=desired_distances,
    R=R,
    learning_rate=0.05,
    steps_per_waypoint=20
)