import random

# Idk what it means by list of lists

password = str(random.randint(0, 9999)).rjust(4, "0")

# Solve
guess = ""
for i in range(10000):
    guess = str(i).rjust(4, "0")

    if guess == password:
        break

print(password, guess)
