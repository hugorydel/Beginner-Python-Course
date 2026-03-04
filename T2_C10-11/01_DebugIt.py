# Goal: Fix the code so it keeps asking for an age until the user enters a valid whole number.
# Expected behaviour (example):
# Enter your age: hello
# Please enter a valid number.
# Enter your age: 19
# Next year you will be 20

while True
    try:
        age = int(input("Enter your age: "))
        print("Next year you will be " + age + 1)
        break
    except
        print("Please enter a valid number.")