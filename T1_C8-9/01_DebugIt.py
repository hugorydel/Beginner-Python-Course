import random

# 1. Generate a random number
# Error here?
ticket = random.randINT(1, 10) 

has_bonus = True

# 2. Check for a win
# Two errors on this line?
if ticket == 10 AND has_bonus:
    print("Jackpot Winner!")
else:
    print("No prize today.")