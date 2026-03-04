# Goal: Edit this code so it keeps asking for numbers and adds them to a running total.
# The loop should stop when the user types "stop" and then print the total.
# Invalid number inputs should not crash the program.
# Expected behaviour (example):
# Enter a number (or stop): 4
# Enter a number (or stop): x
# Invalid input
# Enter a number (or stop): 6
# Enter a number (or stop): stop
# Total: 10

total = 0

while True:
    entry = input("Enter a number (or stop): ")

    if entry == "stop":
        break

    try:
        num = int(entry)
        total = num
    except:
        print("Invalid input")

print("Total:", total)
