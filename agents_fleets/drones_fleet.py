from agents.drone import Drone
from functions.positions_plot import initialize_plot, update_plot
import matplotlib.pyplot as plt
import numpy as np

class DronesFleet:
    def __init__(self, n_drones):
        # Ensure we have exactly 5 drones for a pentagon
        if n_drones != 5:
            raise ValueError("Pentagon formation requires exactly 5 drones.")
        
        # Calculate the positions of a regular pentagon centered at the origin
        radius = 1  # Adjust radius as needed
        angles = np.linspace(0, 2 * np.pi, n_drones, endpoint=False)
        spawning_positions = [[-2 + radius * np.cos(angle), -2 + radius * np.sin(angle), 0] for angle in angles]
        
        self.drones = [Drone(spawning_positions[i], i + 1) for i in range(n_drones)]
        self.n_drones = n_drones
        
        # Initialize visualization for the fleet
        self.fig, self.ax, self.artists = initialize_plot()
        self.agent_types = {drone.agent_name: drone.agent_type for drone in self.drones}

    def formation_with_waypoints(self, waypoints_list, desired_distances, R, learning_rate=0.05, steps_per_waypoint=20):
        for waypoint in waypoints_list:
            centroid = np.mean([drone.agent_position for drone in self.drones], axis=0)
            shift = np.array(waypoint) - centroid

            shift_steps = steps_per_waypoint
            shift_increment = shift / shift_steps

            for step in range(shift_steps):
                for drone in self.drones:
                    drone.agent_position += shift_increment

                self.control_formation(desired_distances, R, learning_rate, 1)

    def control_formation(self, desired_distances, R, learning_rate=0.05, steps=1):
        eps = 1e-6

        for step in range(steps):
            position_updates = np.zeros((self.n_drones, 3))

            for i in range(self.n_drones):
                xi = np.array(self.drones[i].agent_position)
                for j in range(self.n_drones):
                    if i == j:
                        continue
                    xj = np.array(self.drones[j].agent_position)
                    dij = desired_distances[i][j]

                    distance = np.linalg.norm(xi - xj) + eps
                    direction = (xi - xj) / distance

                    if distance <= R:
                        gradient = (distance - dij) * direction
                        position_updates[i] -= learning_rate * gradient

            for i in range(self.n_drones):
                self.drones[i].agent_position += position_updates[i]

            agents_positions = {drone.agent_name: (drone.agent_position[0], drone.agent_position[1]) for drone in self.drones}
            update_plot(agents_positions, self.ax, self.artists, self.agent_types)
            plt.pause(0.01)