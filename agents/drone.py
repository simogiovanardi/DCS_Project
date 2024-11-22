from agents.worker import Worker
import json


class Drone(Worker):
    # Mother_boat class
    def __init__(self, agent_list_position):
        # By default, the mother boat is called "Mother Boat"
        super().__init__("Drone", "Drone", agent_list_position)


