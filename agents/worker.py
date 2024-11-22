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

    def update_position(self, new_position):
        self.agent_list_position[0] = new_position[0],
        self.agent_list_position[1] = new_position[1],
        self.agent_list_position[2] = new_position[2]
