# Edit this program by validating the user's input in the 'output_sequence' function
# - The input must be an integer greater than 0
def output_sequence():
    number = int(input("Enter the final number of the sequence: "))
    for current_number in range(number):
        print(current_number)


output_sequence()
