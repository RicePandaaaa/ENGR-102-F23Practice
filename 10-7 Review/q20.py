"""
Sheldon Cooper's (of Big Bang Theory) favorite number is 73. One of his reasons is that 73 is a prime number
and there are 21 prime numbers between 1 and 73. A prime number is a number greater than 1 that is not
divisible by another number (the only even number that is a prime number is 2; all other prime numbers are
odd). Write the Python code to calculate and print the prime numbers between 1 and 73 (but not including
73). Your program will also need to count the prime numbers to see if this is really the 21th prime number
"""

# Remaining numbers
numbers = list(range(2, 73))

# Loop through every index
index = 0

while index < len(numbers):
    # Every number we hit is prime
    number = numbers[index]

    # Remove every multiple of said number
    for i in range(number + number, 73, number):
        if i in numbers:
            numbers.remove(i)

    index += 1

# Output
print(numbers, len(numbers))
