# Take input
x = float(input("Enter a value between -1 and 1: "))

# Set values
exact_value = 1 / (1 - x)
difference_maximum = 1e-6

# Loop until done
current_sum = 0
current_power = 0

# Check the term versus the difference alloted
while abs(x ** current_power) > difference_maximum:
    current_sum += x ** current_power
    current_power += 1

print(exact_value, current_sum, abs(current_sum - exact_value))
