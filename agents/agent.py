import json

#TODO: fix the agent_list_position to be a 3 element tuple
class Agent:
    # this class is due to the creation of all the simulation's agents
    def __init__(self, agent_name, agent_type, agent_list_position):
        self.agent_name = agent_name
        self.agent_type = agent_type
        self.agent_list_position = agent_list_position

    def get_json_agent_description(self):
        # returns a json of the agent information
        description_dict = {
            "agent_name": self.agent_name,
            "agent_type": self.agent_type,
        }

        return json.dumps(description_dict)

    def get_json_agent_position(self):
        # returns a json of the position X,Y,Z
        position_dict = {

            "X_agent_position": self.agent_list_position[0],
            "Y_agent_position": self.agent_list_position[1],
            "Z_agent_position": self.agent_list_position[2],
        }

        return json.dumps(position_dict)

    # TODO: is the orientation needed?
