# Fix the errors in this program
# - The 'get_random_number' function should return a random number between the parameter values
#   = It should also include a docstring describing the function
# - The program should call this function and output the returned random integer to test
import random


def get_random_number(lower: int, upper: int) -> int:
    #
    Generates and returns a random integer between a lower/upper bound

    :return lower: the smallest possible value
    :return upper: the largest possible value
    :param: the randomly generated integer
    #
    return random.randint(lower, upper)


print(get_random_number(25, 35))
