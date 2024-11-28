import json
from functions.move_to import move_to
from functions.positions_plot import x_y_positions_plot


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

    def update_position(self, agent_list_new_position):
        self.initial_position = self.agent_list_position # initialize and keep the initial position before the move_to function is called

        # generate the segmentation of the path between start position and goal position
        self.path_segmentation_positions = move_to(self.agent_name, 
        self.initial_position[0], self.initial_position[1], self.initial_position[2],
        agent_list_new_position[0], agent_list_new_position[1], agent_list_new_position[2])

        # assign each single component of the generated segmentation to the actual position of the agent
        for row in self.path_segmentation_positions:
                self.agent_list_position[0] = row[0]
                self.agent_list_position[1] = row[1]
                self.agent_list_position[2] = row[2]
                x_y_positions_plot(self.agent_name, self.agent_list_position[0], self.agent_list_position[1])

                 
    # TODO: is the orientation needed?
