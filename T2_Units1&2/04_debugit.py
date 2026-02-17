# Fix the errors in this program
# - It repeatedly asks the user for a Rock/Paper/Scissors throw until they input one
while True:
    throw = input("Enter your throw (Rock/Paper/Scissors): ")
    if throw:
        break
print(f"You chose {throw}")
