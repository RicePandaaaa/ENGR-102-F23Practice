from math import e

# Preset values
TOL = 1e-6
start = 1

# Loop until tolerance met
next_term = 1
current_n = 1
while next_term >= TOL:
    current_n += 1
    start += next_term

    # Calculate next term
    denominator = 1
    for i in range(2, current_n+1):
        denominator *= i

    next_term = 1 / denominator

print(e, next_term)