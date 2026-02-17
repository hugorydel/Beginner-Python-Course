# Edit this program by adding some input validation
# - Ensure both inputs from the user are integers that are greater than 0
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
if num_1 > num_2:
    print(f"The larger number is {num_1}")
else:
    print(f"The larger number is {num_2}")
