# Goal: Fix the code so it prints a numbered to-do list.
# Expected output:
# 1. revise
# 2. email tutor
# 3. exercise

tasks = ["revise", "email tutor", "exercise"]

for i in range(len(tasks) + 1):
    print(i + 1, ".", tasks[i])
