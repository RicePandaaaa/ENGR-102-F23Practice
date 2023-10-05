# Take bounds
lower_bound = int(input("Enter the first integer: "))
upper_bound = int(input("Enter the second integer: "))

multiples = []

# Make the for loop
for number in range(lower_bound, upper_bound + 1):
    # Multiples of 5 and 7 are multiples of 35
    if number % 35 == 0:
        multiples.append(str(number))


# Output
print(f"Multiples: {', '.join(multiples)}")