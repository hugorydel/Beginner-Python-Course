# Fix the errors in this program
# - The program should repeatedly ask the user for two integers
#   = Both must be positive (greater than or equal to 0)
# - It then outputs the average of those two numbers
while True:
    num_1 = int(input("Enter the first positive number: "))
    num_2 = int(input("Enter the second positive number: "))
    if num_1 < 0 and num_2 < 0:
        break
print(f"The average of {num_1} and {num_2} is {(num_1 + num_2) / 2}")
