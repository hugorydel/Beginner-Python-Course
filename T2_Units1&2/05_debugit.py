# Fix the errors in this program
# - It should ask the user for two numbers
#   = The program should not crash if the user inputs a non-integer value
# - It then outputs the larger of the two numbers
catch:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if num2 > num1:
        print(f"{num2} is the larger number")
    elif num1 > num2:
        print(f"{num1} is the larger number")
    else:
        print("They are the same number")
exception:
    print("Please input an integer next time...")
