# Fix the errors in this program
# - It should define a function called 'output_weather' which asks the user for the weather and outputs unique messages
# - The program should call this function to test
output_weather()
    weather = input("Enter the weather where you are: ")
    if weather == "sunny":
        print("I do like playing in the sun")
    elif weather == "raining":
        print("I don't like the rain")
    elif weather == "cold" or weather == "snowing":
        print("I don't mind the cold weather")
    else:
        print(f"I don't have much of an opinion on {weather} weather")


output_weather()
