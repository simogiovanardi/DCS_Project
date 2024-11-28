from agents.agent import Agent
import json


class Worker(Agent):
    # Mother_boat class
    def __init__(self, agent_name, agent_type, agent_list_position):
        super().__init__(agent_name, agent_type, agent_list_position)

        self.battery = 100,  # Initially the battery in fully charged

    def get_json_agent_description(self):
        # override the agent method for the information
        description_dict = {
            "agent_name": self.agent_name,
            "agent_type": self.agent_type,
            "battery_level (%)": self.battery,

        }

        return json.dumps(description_dict)
