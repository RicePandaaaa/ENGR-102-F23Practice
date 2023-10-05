# Store values
total = 0
count = 0
highest = "N/A"
lowest = "N/A"

# Take input and loop
number = float(input("Enter a positive number: "))

while number >= 0:
    # Set highest and lowest
    if count == 0:
        highest = number
        lowest = number

    # Update highest and lowest
    highest = max(highest, number)
    lowest = min(lowest, number)

    # Update values
    total += number
    count += 1

    number = float(input("Enter a positive number: "))

# Output
average = "N/A"
if count != 0:
    average = total / count

print(f"The maximum number is: {highest}")
print(f"The minimum number is: {lowest}")
print(f"The average is: {average}")
