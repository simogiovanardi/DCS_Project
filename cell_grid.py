from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import json

# Connect to CoppeliaSim
client = RemoteAPIClient()
sim = client.getObject('sim')

# Load the JSON file
with open('map.json', 'r') as file:
    matrix = json.load(file)

# Get the number of rows and columns
rows = len(matrix)
cols = len(matrix[0])

# Start the simulation
sim.startSimulation()

for row in range(1, rows + 1):  # Loop from 1 to rows
    for col in range(1, cols + 1):  # Loop from 1 to cols
        # Construct the cell name based on row and col
        cell_name = f"/Map/Cell_{row}_{col}"
        cell_handle = sim.getObject(cell_name)

        # Check if the cell handle is valid before applying color
        if cell_handle != -1:
            # Get the matrix value and calculate RGB grayscale
            gray_value = matrix[row - 1][col - 1]  # Adjust for 0-based indexing
            rgb_value = 255 - (gray_value * 2.55)
            rgb_list = [rgb_value, rgb_value, rgb_value]

            # Debugging prints
            print(f"Cell[{row},{col}] - Matrix Value: {gray_value}, RGB: {rgb_list}")

            # Apply color to the cell
            sim.setShapeColor(cell_handle, None, sim.colorcomponent_ambient_diffuse, rgb_list)
        else:
            print(f"Warning: {cell_name} not found in CoppeliaSim")

# Stop the simulation
sim.stopSimulation()
