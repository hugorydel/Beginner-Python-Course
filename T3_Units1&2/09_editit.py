# Edit this program by asking the user for two values
# - The size of the shape to output
# - The type of shape (0/1/2) to output
#   = Validate both inputs so they are integers
#       == The size must be greater than 1
#       == The type must be 0, 1, or 2
# Call the function using these user input values as arguments
def output_shape(size: int, shape_type: int):
    if shape_type == 0:
        for row in range(size):
            line = ""
            for col in range(size):
                line += "R"
            print(line)
    elif shape_type == 1:
        for row in range(size):
            line = ""
            for col in range(row + 1):
                line += "T"
            print(line)
    elif shape_type == 2:
        for row in range(size // 2 - 1):
            line = ""
            for col in range(size // 2 - row - 1):
                line += " "
            for col in range(row * 2 + 1):
                line += "D"
            print(line)
        for row in range(size // 2):
            line = ""
            for col in range(row):
                line += " "
            for col in range(size - row * 2 - 1):
                line += "D"
            print(line)
