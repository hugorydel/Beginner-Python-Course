# Fix the errors in this program
# - It should repeatedly ask the user for two numbers
# - It then calculates and outputs the average of those numbers
if True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The average of {num1} and {num2} is {(num1 + num2) / 2}")
    except ValueError:
        print("Please input an integer...")
