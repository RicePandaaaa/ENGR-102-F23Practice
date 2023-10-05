# Get the two numbers
num1 = int(input("Enter integer 1: "))
num2 = int(input("Enter integer 2: "))

# Case: num2 < num1
if num2 < num1:
    print("Invalid input!")

else:
    total = 0
    # Loop through possible numbers
    while num1 <= num2:
        # Check for divisibility
        if num1 % 4 == 0:
            total += num1

        num1 += 1

    print(f"The sum of multiples of 4 between 2 and 12 is: {total}")

