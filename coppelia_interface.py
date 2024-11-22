from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import json

client = RemoteAPIClient()
sim = client.getObject('sim')

# Load the JSON file
with open('map.json', 'r') as file:
    matrix = json.load(file)

print(matrix)
rows = len(matrix) + 1
cols = len(matrix[0]) + 1



position_list = [-2.5, 2.5, 0]

for row in range(1, rows):
    if row != 1:
        position_list[0] = position_list[0] + 0.5
    for col in range(1, cols):
        cell_name = f"/Map/Cell_{row}_{col}"
        cell_handle = sim.getObject(cell_name)
        # Change the color of the map if in the generated matrix a value different from zero is present
        rgb_value = 1-((matrix[row-1][col-1])/100)  # Color logic: from 100-scale to 0-1 value
        rgb_list = [rgb_value, rgb_value, rgb_value]
        # Apply color to the cell
        sim.setShapeColor(cell_handle, None, sim.colorcomponent_ambient_diffuse, rgb_list)

        # Set the desired height (Z-axis scale factor)
        # Scale the cube along the Z-axis only (keep X and Y scaling factors at 1 to avoid changing them)
        sim.setObjectPosition(cell_handle, position_list)
        # sim.scaleObject(cell_handle, 1, 1, 10)

