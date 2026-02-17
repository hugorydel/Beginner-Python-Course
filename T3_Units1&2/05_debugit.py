# Fix the errors in this program
# - It should define a function called 'output_pet_information' which asks the user for information on a pet
#   = It outputs this information in a formatted list
# - The program should call this function to test
def output_pet_information()
print("Enter the following information about your pet:")
name = input("\tName: ")
age = int(input("\tAge: "))
        species = input("\tSpecies: ")
        food = input("\tFavourite Food: ")
        print("Thank you for this information!")
        print("To summarise:")
print(f"\tYour pet is called {name}")
print(f"\tThey are {age} years old")
print(f"\tThey are a {species}")
print(f"\tThey like eating {food}")


output_pet_information()
