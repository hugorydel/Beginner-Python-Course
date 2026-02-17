# Edit this while loop so it is 'infinite'
# - It should repeatedly ask the user for a number
#   = It should only stop asking if that number is positive (greater than or equal to 0)
counter = 10
while counter > 0:
    number = int(input("Enter a positive number: "))
    counter += 1
print(f"You chose {number}")
