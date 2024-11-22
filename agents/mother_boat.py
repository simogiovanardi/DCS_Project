from agents.agent import Agent
import json


class MotherBoat(Agent):
    # Mother_boat class
    def __init__(self, agent_list_position):
        # By default, the mother boat is called "Mother Boat"
        super().__init__("Mother Boat", "Mother_Boat", agent_list_position)
