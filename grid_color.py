from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import random

client = RemoteAPIClient()
sim = client.getObject('sim')

# Grid dimensions
cols = 5  # Define the grid size (e.g., 5x5)

sim.startSimulation()

# Example logic: Random color generation for each cell
for col in range(1,cols):
    cell_name = f"/Cell{col}"  # Assuming cells are named this way in CoppeliaSim
    print(cell_name)
    cell_handle = sim.getObject(cell_name)

    # Define color logic (random in this case)
    color = [random.random(), random.random(), random.random()]  # RGB color with values [0, 1]

    # Apply color to the cell
    sim.setShapeColor(cell_handle, None, sim.colorcomponent_ambient_diffuse, color)


sim.stopSimulation()
