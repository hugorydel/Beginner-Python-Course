# Edit this program by defining two functions for this program code
# - The first function should create the list of numbers
# - The second function should sort a parameter list of numbers in descending order
# Call both functions in the correct order so that the program behaves as it does before any of your edits
numbers = []
while True:
    choice = input("Would you like to add another number to the list (yes/no): ")
    if choice == "yes":
        number = int(input("\tEnter the number to add: "))
    elif choice == "no":
        break
for _ in range(len(numbers)):
    for index in range(len(numbers) - 1):
        if numbers[index] < numbers[index + 1]:
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
print(f"The numbers in descending order are: {numbers}")
