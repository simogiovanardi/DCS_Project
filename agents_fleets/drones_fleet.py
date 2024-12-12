from agents.drone import Drone
from functions.positions_plot import initialize_plot, update_plot
import matplotlib.pyplot as plt  # Add this import
import numpy as np

class DronesFleet:
    def __init__(self, n_drones):
        spawning_position = [-2, 2, 0]
        self.drones = [Drone(spawning_position, i+1) for i in range(n_drones)] # gives a name to each drone (i+1 since it starts from zero)
        self.n_drones = n_drones

        # Initialize visualization for the fleet
        self.fig, self.ax, self.artists = initialize_plot()
        self.agent_types = {drone.agent_name: drone.agent_type for drone in self.drones}


    def move_drones(self, new_positions, velocity):
        """
        Move drones to new positions with the specified velocity, and visualize their trajectories.

        :param new_positions: List of new positions [(x,y,z), ...] for each drone.
        :param velocity: Speed of movement.
        """
        # Ensure the number of new positions matches the number of drones
        # Ensure the number of new positions matches the number of drones
        if len(new_positions) != self.n_drones:
            raise ValueError("Number of new positions must match the number of drones.")
        
        # Move drones and collect their positions over time
        all_positions_over_time = []

        for i in range(self.n_drones):
            pos_over_time = self.drones[i].move_to(new_positions[i], velocity)
            all_positions_over_time.append(pos_over_time)
            
        # Now, determine the maximum number of time steps
        max_time_steps = max(len(pos_list) for pos_list in all_positions_over_time)

        # Loop over time steps
        for t in range(max_time_steps):
            agents_positions = {}
            for i, pos_list in enumerate(all_positions_over_time):
                if t < len(pos_list):
                    x, y, z, time_stamp = pos_list[t]
                    # Update the drone's position
                    self.drones[i].agent_position = [x, y, z]
                else:
                    # If this drone has no more positions, keep the last one
                    pass

                agents_positions[self.drones[i].agent_name] = (
                    self.drones[i].agent_position[0],
                    self.drones[i].agent_position[1],
                )

            # Update the plot with current agent positions
            update_plot(agents_positions, self.ax, self.artists, self.agent_types)
            
            # Pause to create animation effect
            plt.pause(0.1)  # Adjust pause duration as needed

        # Return all positions over time if needed
        return all_positions_over_time
    

    def formation_with_waypoints(self, waypoints_list, desired_distances, R, learning_rate=0.01, steps_per_waypoint=100):
        """
        Move the fleet in formation while the centroid follows waypoints.

        :param waypoints_list: List of waypoints [ [x,y,z], ... ] for the formation's centroid.
        :param desired_distances: Matrix of desired distances `d_ij` for all drone pairs.
        :param R: Maximum allowed interaction range.
        :param learning_rate: Learning rate for gradient descent.
        :param steps_per_waypoint: Gradient descent steps for each waypoint.
        """
        for waypoint in waypoints_list:
            # Calculate the centroid of the current drone positions
            centroid = np.mean([drone.agent_position for drone in self.drones], axis=0)
            shift = np.array(waypoint) - centroid

            # Shift the formation towards the waypoint
            for drone in self.drones:
                drone.agent_position += shift

            # Perform formation control to maintain structure
            self.control_formation(desired_distances, R, learning_rate, steps_per_waypoint)

    



    def compute_weight(self, xi, xj, d, R):
        """
        Compute the weight w_ij between two agents based on their positions and desired distance.

        :param xi: Position of agent i as [x, y].
        :param xj: Position of agent j as [x, y].
        :param d: Desired distance between agents i and j.
        :param R: Maximum allowed interaction range.
        :return: Weight w_ij.
        """
        distance = np.linalg.norm(np.array(xi) - np.array(xj))

        # Handle divide by zero case
        if distance == 0:
            return 0  # No force if the two agents completely overlap
    
        if distance >= R:
            return 0  # No interaction if distance exceeds R
        return (1 - d / distance) / ((R - distance) ** 3)



    def control_formation(self, desired_distances, R, learning_rate=0.01, steps=100):
        """
        Perform formation control using the formation + connectivity approach.

        :param desired_distances: Matrix of desired distances `d_ij` for all drone pairs.
        :param R: Maximum allowed interaction range.
        :param learning_rate: Learning rate for gradient descent.
        :param steps: Number of gradient descent steps.
        """
        if len(desired_distances) != self.n_drones or len(desired_distances[0]) != self.n_drones:
            raise ValueError("Desired distances matrix must match the number of drones.")

        # Small epsilon for numerical stability
        eps = 1e-6

        for step in range(steps):
            # Compute position updates for each drone
            position_updates = np.zeros((self.n_drones, 3))

            for i in range(self.n_drones):
                for j in range(self.n_drones):
                    if i == j:
                        continue
                    xi = np.array(self.drones[i].agent_position)
                    xj = np.array(self.drones[j].agent_position)
                    dij = desired_distances[i][j]
                    
                    # Compute distance
                    distance = np.linalg.norm(xi - xj)
                    
                    # If drones are too close or too far, skip the interaction
                    if distance == 0 or distance >= R:
                        continue

                    # Compute interaction weight
                    weight = self.compute_weight(xi[:2], xj[:2], dij, R)

                    if weight != 0:
                        # Avoid division by zero using epsilon during direction normalization
                        direction = (xi - xj) / (distance + eps)
                        
                        # Compute gradient of potential energy
                        gradient = weight * (dij - distance) * direction

                        # Update position increment for drone i
                        position_updates[i] += learning_rate * gradient

            # Update the positions of all drones
            for i in range(self.n_drones):
                self.drones[i].agent_position += position_updates[i]

            # Visualize the current positions
            agents_positions = {drone.agent_name: (drone.agent_position[0], drone.agent_position[1]) for drone in self.drones}
            update_plot(agents_positions, self.ax, self.artists, self.agent_types)

            # Pause for visualization during simulation
            plt.pause(0.1)