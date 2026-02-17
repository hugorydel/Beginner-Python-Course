# Edit this program by asking the user for four float values
# - The X and Y values for the starting coordinate
# - The X and Y values for the ending coordinate
# Call the 'output_distance' function using these four values as arguments
import math


def output_distance(x1: float, y1: float, x2: float, y2: float):
    x_length = x2 - x1
    y_length = y2 - y1
    distance = math.sqrt(x_length * x_length + y_length * y_length)
    print(f"The distance is {distance}")
