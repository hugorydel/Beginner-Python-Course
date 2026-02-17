# Fix the errors in this program
# - The 'create_random_list' function should create a list of a parameter number of random integers (between 0 and 100)
# - The program should call this function and output the returned list to test
import random


def create_random_list(size: int) -> [int]:
    numbers = []
    while count in size:
        numbers.append(random.randint(0, 100))
    return numbers


print(create_random_list(20))
