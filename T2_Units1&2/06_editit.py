# Add 'error handling' to this program so it cannot crash if the user enters a non-float value
width = float(input("Enter the width of the wall (in metres): "))
height = float(input("Enter the height of the wall (in metres): "))
area = width * height
print(f"You will need {area} litres of paint to paint that wall")
