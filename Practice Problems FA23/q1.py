# Take the input
number = int(input("Enter an integer between 100 and 1000000, inclusive: "))

# Verify the input
if number < 100 or number > 1000000:
    print("Wrong input!\n")
    number = int(input("Enter an integer between 100 and 1000000, inclusive: "))

else:
    # Extract the two digits
    last_digit = number % 10
    number //= 10
    second_to_last_digit = number % 10

    # Check if both even, odd, or mixed and do appropriate output
    if last_digit % 2 == 0 and second_to_last_digit % 2 == 0:
        # Calculate sum
        total = last_digit + second_to_last_digit
        print(f"Both even! Sum = {total}\n")

    elif last_digit % 2 == 1 and second_to_last_digit % 2 == 1:
        # Calculate product
        product = last_digit * second_to_last_digit
        print(f"Both odd! Product = {product}\n")

    else:
        print("One odd, one even.\n")
