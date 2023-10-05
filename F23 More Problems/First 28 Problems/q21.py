from math import log

# Take input
x = float(input("Enter a value between -1 and 1: "))

while not (-1 < x < 1):
    x = float(input("Enter a value between -1 and 1: "))

# Set values
TOL = 1e-6
n = 1
total = 0

# Function to calculate the next term
def term(x, n):
    return (2 / (2 * n - 1)) * (x ** (2 * n - 1))

# Loop until done
while term(x, n) >= TOL:
    total += term(x, n)
    n += 1

# Verify
print(log((1 + x) / (1 - x)), total, term(x, n))