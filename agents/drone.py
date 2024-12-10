from agents import Agent
import json


class Drone(Agent):
    # Drone class
    def __init__(self, agent_list_position, number):
        # By default, the mother boat is called "Mother Boat"
        super().__init__(f"Drone{number}", "Drone", agent_list_position)   
        self.battery = 100,  # Initially the battery in fully charged
        

    def get_json_agent_description(self):
        # override the agent method for the information
        description_dict = {
            "agent_name": self.agent_name,
            "agent_type": self.agent_type,
            "battery_level (%)": self.battery,
        }
        return json.dumps(description_dict)

