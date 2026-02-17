# Edit this program by adding 6 random integers to the numbers list
# - They should all go after the current numbers in the list
numbers = [10, 4, 8, 11]

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print(f"The smallest number in the list {numbers} is {smallest}")
