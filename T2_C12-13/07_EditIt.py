# Goal: Edit this code so it sums only the positive numbers in the list.
# Expected output:
# Positive sum: 16

nums = [5, -2, 8, -1, 3, -4]
total = 0

for num in nums:
    total = total + num

print("Positive sum:", total)
