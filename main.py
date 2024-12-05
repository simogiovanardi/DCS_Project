from agents.vessel import Vessel
from functions.move_to import move_to
from functions.positions_plot import initialize_plot

# initialization of the plot where all the agents can be seen
# fig, ax, artists = initialize_plot(xlim=(-10, 10), ylim=(10, 10))



# drone1 = Drone([0,0,0], 1)
vessel1 = Vessel([1,2,3])
print(f"drone spawned in {vessel1.agent_list_position}")


vessel1.update_position([1,1,0])
# print(f"check the actual position after saying to change position: {drone1.agent_list_position}")

vessel2 = Vessel([0,1,4])

vessel2.update_position([0.5,3,0])

# drone2 = Drone([0,0,0], 2)
# print(drone2.agent_list_position)
# drone2.update_position([4,2,0])
# print(drone2.agent_list_position)


# print(move_to("ciccio", 0,0,0,1, 2, 3))
