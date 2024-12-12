def generate_zigzag(rows, cols, height):
    zigzag_path = []
    for col in range(cols):
        if col % 2 == 0:  # Even column: top-to-bottom
            for row in range(rows):
                zigzag_path.append([row, col, height])
        else:  # Odd column: bottom-to-top
            for row in range(rows - 1, -1, -1):
                zigzag_path.append([row, col, height])
    return zigzag_path
