# Take input
numbers = []
duplicate_found = False

for i in range(5):
    number = int(input("Enter an integer: "))
    
    # Check for duplicates
    duplicate_found = duplicate_found or number in numbers

    # Add number to known numbers
    numbers.append(number)

if duplicate_found:
    print("Duplicates")
else:
    print("All Unique")