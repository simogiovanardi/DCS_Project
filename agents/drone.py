from agents.worker import Worker
import json


class Drone(Worker):
    # Drone class
    def __init__(self, agent_list_position, number):
        # By default, the mother boat is called "Mother Boat"
        super().__init__(f"Drone{number}", "Drone", agent_list_position)


