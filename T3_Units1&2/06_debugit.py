# Fix the errors in this program
# - It should define a function called 'output_conversion' which takes a float parameter for an amount, and a string parameter for a target unit
#   = It outputs the amount (from metres) converted to the target amount
# - The program should call this function using the arguments 2000 and "mi" to test
def output_conversion(amount: str, targeting):
    if target == "m":
        print(amount)
    elif target == "km":
        print(amount / 1000.0)
    elif target == "mi":
        print(amount / 1609.0)


output_conversion(2000, "mi")
