# Goal: Find and fix the 3 errors preventing this "Lucky Draw" game from running.
# Error below
include random

# 1. Generate a random number
# Error below
ticket = random.RANDINT(1, 10) 

has_bonus = True

# 2. Check for a win
# Errors on below line
if ticket == 10 not has_bonus:
    print("Jackpot Winner!")
else:
    print("No prize today.")