from agents_fleets.drones_fleet import DronesFleet
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from functions.positions_plot import initialize_plot, get_agent_style


fleet1 = DronesFleet(1)

"""
updated_positions = [[5,3,5],[2,5,7],[9,7,4]]
fleet1.move_drones(updated_positions, 1)

updated_positions = [[1,3,5],[8,5,7],[2,7,4]]
fleet1.move_drones(updated_positions, 1)
"""

cols = 10
rows = 10 
height = 2
waypoints_list = []
for col in range(cols):
    for row in range(rows):
        waypoints_list.append([col,row,height])

for i in waypoints_list:
    fleet1.move_drones(i, 2)