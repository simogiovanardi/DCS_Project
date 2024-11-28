import math

# this function dicretizes the path to be walked by an agent in many steps

def move_to(name, actual_X, actual_Y, actual_Z, new_X, new_Y, new_Z):   # velocity expressed in [m/s]

    path_lenght = math.sqrt((abs(actual_X - new_X))**2 + (abs(actual_Y - new_Y))**2 + (abs(actual_Z - new_Z))**2)
    # euclidean norm

    n_steps = round(20 * path_lenght) # discretization of the distance (start to end) dependent on the lenght

    steps = []

    x_lenght_step = abs(actual_X - new_X)/n_steps
    y_lenght_step = abs(actual_Y - new_Y)/n_steps
    z_lenght_step = abs(actual_Z - new_Z)/n_steps

    for i in range(n_steps+1):
        steps.append([round((actual_X + (i*x_lenght_step)),2), round((actual_Y + (i*y_lenght_step)),2), round((actual_Z + (i*z_lenght_step)),2)])
    
    return steps


