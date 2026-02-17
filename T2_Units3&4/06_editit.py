# Edit this program by adding 5 numbers to the numbers list
# - The numbers should be: 12, 31, 9, 20, -6
numbers = []
num_evens = 0
num_odds = 0
for number in numbers:
    if number % 2 == 0:
        num_evens += 1
    else:
        num_odds += 1
print(f"The list {numbers} contains {num_evens} even numbers and {num_odds} odd numbers")
