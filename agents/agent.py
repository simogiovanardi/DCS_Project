import json
from functions.move_to import move_to

class Agent:
    def __init__(self, agent_name, agent_type, agent_position):
        self.agent_name = agent_name
        self.agent_type = agent_type
        self.agent_position = agent_position  # [x, y, z]

    def get_json_agent_description(self):
        description_dict = {
            "agent_name": self.agent_name,
            "agent_type": self.agent_type,
        }
        return json.dumps(description_dict)

    def get_json_agent_position(self):
        position_dict = {
            "X_agent_position": self.agent_position[0],
            "Y_agent_position": self.agent_position[1],
            "Z_agent_position": self.agent_position[2],
        }
        return json.dumps(position_dict)

    def move_to(self, new_position, velocity=1):
        self.initial_position = self.agent_position.copy()
        self.path_segmentation_positions = move_to(
            self.initial_position[0], self.initial_position[1], self.initial_position[2],
            new_position[0], new_position[1], new_position[2], velocity
        )

        positions_over_time = []

        for pos in self.path_segmentation_positions:
            x, y, z, t = pos
            self.agent_position = [x, y, z]
            positions_over_time.append((x, y, z, t))

        return positions_over_time
    