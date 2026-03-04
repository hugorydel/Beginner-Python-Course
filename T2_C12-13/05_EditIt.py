# Goal: Edit this code so it correctly prints the largest number in the list.
# Expected output:
# Largest: 19

nums = [11, 4, 19, 7, 13]
largest = 0

for num in nums:
    if num < largest:
        largest = num

print("Largest:", largest)
