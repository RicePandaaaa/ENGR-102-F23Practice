# Get input
n = int(input("Enter n: "))

while n >= 0 or n == -1:
    # Edge cases
    if n == 0 or n == -1:
        print(1)
        n = int(input("Enter n: "))
        continue

    # Calculate the double factorial
    product = 1
    for i in range(n, 0, -2):
        product *= i

    # Output and get next input
    print(product)
    n = int(input("Enter n: "))