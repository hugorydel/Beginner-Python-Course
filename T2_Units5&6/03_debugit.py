# Fix the errors in this program
# - The program should create a blank list
# - It should then add 10 random integers to the list (all between 0 and 100, inclusive)
import random

numbers = []
for count in range(10):
    numbers.pop(random.randint(0, 100))
print(numbers)
