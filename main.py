from agents.drone import Drone
from functions.move_to import move_to


drone1 = Drone([0,0,0], 1)
print(f"drone spawned in {drone1.agent_list_position}")

drone1.update_position([1,1,0])
print(f"check the actual position after saying to change position: {drone1.agent_list_position}")


# drone2 = Drone([0,0,0], 2)
# print(drone2.agent_list_position)
# drone2.update_position([4,2,0])
# print(drone2.agent_list_position)


# print(move_to("ciccio", 0,0,0,1, 2, 3))
