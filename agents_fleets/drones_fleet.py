from agents.drone import Drone
from functions.positions_plot import initialize_plot, update_plot
import matplotlib.pyplot as plt  # Add this import

class DronesFleet:
    def __init__(self, n_drones):
        spawning_position = [-2, 2, 0]
        self.drones = [Drone(spawning_position.copy(), i+1) for i in range(n_drones)]
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
            plt.pause(0.01)  # Adjust pause duration as needed

        # Return all positions over time if needed
        return all_positions_over_time
    

        # def formation_control():
            