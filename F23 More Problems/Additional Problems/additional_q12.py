# Preset values
count = 0
minumum = -1
maximum = -1

# Get ages
age = int(input("Enter a number (negative to exit): "))

while age >= 0:
    # Update min and max
    if count == 0:
        minumum = age
        maximum = age

    # Compare and replace (if needed)
    minumum = min(minumum, age)
    maximum = max(maximum, age)

    # Update count and get next age
    count += 1
    age = int(input("Enter a number (negative to exit): "))

# Output
print("Number of people  Minimum age  Maximum age")
print(str(count).ljust(len("Number of people  ")), end="")
print(str(minumum).ljust(len("Minimum age  ")), end="")
print(maximum)