primes = []

numbers = list(range(2, 73))

# Function to remove non-primes
def filter(prime):
    for i in range(prime * 2, 73, prime):
        if i in numbers:
            numbers.remove(i)

# Loop through the numbers
current_index = 0
while current_index < len(numbers):
    current_number = numbers[current_index]

    # Prime number
    if current_number not in primes:
        filter(current_number)

    current_index += 1

# Output
print(numbers, len(numbers))
