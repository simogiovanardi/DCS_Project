from agents.worker import Worker
import json


class Vessel(Worker):
    # Mother_boat class
    def __init__(self, agent_list_position):
        # By default, the mother boat is called "Mother Boat"
        super().__init__("Vessel", "Vessel", agent_list_position)

        self.payload = 0  # Initially the boat is empty (no garbage in it)

    def get_json_agent_description(self):
        # override the agent method for the information
        description_dict = {
            "agent_name": self.agent_name,
            "agent_type": self.agent_type,
            "vessel_battery (%)": self.battery,
            "vessel_payload (%)": self.payload
        }

        return json.dumps(description_dict)
