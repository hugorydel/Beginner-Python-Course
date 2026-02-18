# Goal: Modify this "Dungeon Trap" logic.
# Change the trap so it triggers on a roll of 1 or 2 (currently only 1).
# Add a new boolean variable: has_shield = True.
# Update the if statement: The trap should only hurt you if the roll is low AND you do not have a shield.

import random

roll = random.randint(1, 6)
print(f"You rolled a {roll}")

# --- Edit below this line ---

if roll == 1:
    print("The trap hits you! -10 Health")
else:
    print("You are safe.")
