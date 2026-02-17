# Fix the errors in this program
# - It should define two functions, 'output_rectangle' and 'get_integer_for_rectangle'
#   = 'output_rectangle' should output a rectangle of Os based on the size parameter
#   = 'get_integer_for_rectangle' should get a number from the user, validated between the two parameters
#       == When the user inputs a valid integer, it calls 'output_rectangle' to output a rectangle of that size
# - The program should call 'get_integer_for_rectangle' function with the arguments 5 and 10 to test
def output_rectangle(size: int):
    for row in range(size):
        line = ""
        for col in range(size):
            line += "O"
        print(line)


def get_integer_for_rectangle(minimum: int, maximum: int):
    while True:
        try:
            number = int(input(f"Enter a rectangle to output between {minimum} and {maximum}"))
            if minimum <= number <= maximum:
                output_rectangle()
                break
        except ValueError:
            pass


get_integer_for_rectangle()
