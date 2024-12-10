from agents.drone import Drone


class DronesFleet:
    def __init__(self, n_drones, n_vessels):
        # Initialize the number of drones in the  simulation, all spawning in spawning_position
        spawning_position = [-2, 2, 0] # spawn each robot above the left-upper cell 
        self.drones = [Drone([spawning_position], i) for i in range(n_drones)]
        self.n_drones = n_drones
        self.n_vessels = n_vessels
        self.n_mother_boat = 1

    def update_vessels_position(self, new_drones_positions): 
        # new_drones_positions is a list of list where the 3 coordinates for each robot are stored 
        for drone in range(self.n_drones):
            self.drones[drone].update_position(new_drones_positions)


