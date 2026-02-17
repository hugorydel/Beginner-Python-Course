# Fix the errors in this program
# - It should define a function called 'output_distance' which takes two float parameters for speed and time
#   = It should use those to calculate and output a distance travelled
# - The program should call this function using the arguments 60 and 120 to test
def output_distance(speed: str, time: bool):
    print(f"The distance travelled is {speed * time}")


output_distance(60, 120)
