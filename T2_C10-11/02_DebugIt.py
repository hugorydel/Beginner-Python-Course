# Goal: Edit this code so it keeps asking until the user enters a number greater than 10.
# Expected behaviour (example):
# Enter a number: 4
# Too small
# Enter a number: 10
# Too small
# Enter a number: 13
# Accepted!

number = 0

while number < 10:
    number = int(input("Enter a number: "))
    print("Too small")

print("Accepted!")
