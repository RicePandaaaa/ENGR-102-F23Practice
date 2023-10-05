# Get input and split
numbers = input("Enter five integers: ").split(" ")

# Sort numbers
numbers.sort()

# Check for duplicates
for i in range(4):
    if numbers[i] == numbers[i+1]:
        print("Duplicates")
        break

else:
    print("All Unique")