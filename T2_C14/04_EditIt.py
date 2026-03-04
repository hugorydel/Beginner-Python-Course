# Goal: Fix the code so it returns the largest number in the list.
# Expected output:
# 9


def largest_number(nums):
    largest = nums[0]

    for num in nums:
        if nums > largest:
            largest = num

    print(largest)


print(largest_number([4, 7, 2, 9, 5]))
