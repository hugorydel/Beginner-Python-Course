# Edit this program to add input validation and error handling for the user input
# - The program should only accept positive non-zero values for the radius
# - Make sure the program cannot crash if the user inputs a non-float value
radius = float(input("Enter the radius of the circle (larger than 0) in metres: "))
area = 3.14 * radius * radius
print(f"The area of a circle with a radius of {radius}m is {area}m^2")
