from agents import Agent
import json


class Vessel(Agent):
    # Vessel class
    def __init__(self, agent_list_position, number):
        super().__init__(f"Vessel{number}", "Vessel", agent_list_position)
        self.payload = 0  # Initially the boat is empty (no garbage in it)
        self.battery = 100,  # Initially the battery in fully charged
    
    def get_json_agent_description(self):
        # override the agent method for the information
        description_dict = {
            "agent_name": self.agent_name,
            "agent_type": self.agent_type,
            "vessel_battery (%)": self.battery,
            "vessel_payload (%)": self.payload
        }

        return json.dumps(description_dict)
