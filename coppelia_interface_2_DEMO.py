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

sim.startSimulation()

size = 10
sim.simxAddDrawingObject_cubes(size, final int[] color, final float[] coords, final String topic)
'''
for row in range(1, rows):
    for col in range(1, cols):
        cell_name = f"/Map/Cell_{row}_{col}"
        cell_handle = sim.getObject(cell_name)
        # Change the color of the map if in the generated matrix a value different from zero is present
        rgb_value = int((matrix[row-1][col-1] * 2.55))  # Color logic: from 100-scale to RGB- scale
        rgb_list = [rgb_value, rgb_value, rgb_value]
        # Apply color to the cell
        sim.setShapeColor(cell_handle, None, sim.colorcomponent_ambient_diffuse, rgb_list)

        # Set the desired height (Z-axis scale factor)
        # height_scale = random.random()  # This will double the height of the cube

        # Scale the cube along the Z-axis only (keep X and Y scaling factors at 1 to avoid changing them)
        # sim.scaleObject(cube_handle, 1, 1, height_scale)
'''
sim.stopSimulation()
