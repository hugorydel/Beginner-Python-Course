# Goal: Edit this code so it returns the discounted price correctly.
# Expected output:
# 80.0
# 45.0


def apply_discount(price, percent):
    discount = percent / 100
    return price - discount


print(apply_discount(100, 20))
print(apply_discount(50, 10))
