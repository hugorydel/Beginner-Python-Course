# Goal: Fix the 2 errors in this "Access Control" script.

age = 14
has_permission = False

# 1. Error: Python doesn't use symbols for logic
if age > 12 && age < 18:
    print("You are a teenager.")

# 2. Error: Python uses a word, not a symbol
if !has_permission:
    print("Alert: No permission slip found.")