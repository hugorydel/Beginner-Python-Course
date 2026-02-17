# Edit this program by asking the user for a sport to append to the list
# - Only do this if they want to add another sport to the list
sports = []
while True:
    choice = input("Would you like to add another sport: ")
    if choice == "yes":
        pass
    else:
        break
print("You added the sports:")
for sport in sports:
    print(sport)
