# Fix the errors in this program
# - It generates two random integers between 1 and 30
# - It then calculates and outputs the area for a rectangle made up of those two random integers
width = random.randint(-20, 1)
height = random.random(-20, 1)
area = width * height
print(f"The area of a rectangle with a size of {width}X{height} is {area}")
