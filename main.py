from agents_fleets.drones_fleet import DronesFleet
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from functions.positions_plot import initialize_plot, get_agent_style


fleet1 = DronesFleet(3)

updated_positions = [[5,3,5],[2,5,7],[9,7,4]]
fleet1.move_drones(updated_positions, 1)

updated_positions = [[1,3,5],[8,5,7],[2,7,4]]
fleet1.move_drones(updated_positions, 1)