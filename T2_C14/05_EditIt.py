# Goal: Edit this code so it returns True for even numbers and False for odd numbers.
# Expected output:
# True
# False


def is_even(n):
    if n % 2 == 0:
        return "True"
    else:
        return "False"


print(is_even(4))
print(is_even(7))
