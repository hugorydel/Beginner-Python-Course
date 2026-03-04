# Goal: Fix the code so it does not crash if the user enters invalid input.
# Expected behaviour (example):
# Enter numerator: 10
# Enter denominator: 0
# Invalid input, try again.
# Enter numerator: 10
# Enter denominator: 2
# Result: 5.0

while True:
    try:
        top = int(input("Enter numerator: "))
        bottom = int(input("Enter denominator: "))
        print("Result:", top / bottom)
        break
    except:
        print("Invalid input, try again.")
        break
