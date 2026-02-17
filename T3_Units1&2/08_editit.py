# Edit this program by defining another function which takes a list of integers as a parameter
# - The function should output that list in a bullet point style format
# Call this new function from 'create_list_to_output' after the for loop (that is when the list has been made)
import random


def create_list_to_output(size: int):
    numbers = []
    for _ in range(size):
        numbers.append(random.randint(0, 100))


create_list_to_output(20)
