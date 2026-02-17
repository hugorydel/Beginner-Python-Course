# Edit this program so the while loop is a finite while loop
# - It should continue iterating while the counter is less than the user input amount
amount = int(input("Enter the number of Fibonacci Numbers to output: "))
previous_2 = 0
print(f"The 1 number in the Fibonacci sequence is {previous_2}")
previous_1 = 1
print(f"The 2 number in the Fibonacci sequence is {previous_1}")
counter = 3
while False:
    current = previous_2 + previous_1
    print(f"The {counter} number in the Fibonacci sequence is {current}")
    previous_2 = previous_1
    previous_1 = current
    counter += 1
