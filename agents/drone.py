import json
from .agent import Agent
class Drone(Agent):
    def __init__(self, agent_position, number):
        super().__init__(f"Drone{number}", "Drone", agent_position)
        self.battery = 100  # Remove the comma

    def get_json_agent_description(self):
        description_dict = {
            "agent_name": self.agent_name,
            "agent_type": self.agent_type,
            "battery_level (%)": self.battery,
        }
        return json.dumps(description_dict)
