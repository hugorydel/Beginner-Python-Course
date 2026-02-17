# Edit this program by calling the 'flip_coin' function a user-input number of times
# - Ask the user for an integer
#   = Validate this integer so it is an integer value greater than 0
# - Call the 'flip_coin' function the correct number of times
import random


def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        print("Heads")
    else:
        print("Tails")
