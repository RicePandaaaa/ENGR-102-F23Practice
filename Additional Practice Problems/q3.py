# Take input
name, age = input("Enter the name and age of the next person: ").split()

# Counters
total_age = 0
people_processed = 0

youngest_age = 0
youngest_name = ""

oldest_age = 0
oldest_name = ""

# Main loop
while age != "0":
    # Set youngest and oldest people
    if people_processed == 0:
        youngest_age = int(age)
        oldest_age = int(age)

        youngest_name = name
        oldest_name = name

    # Compare youngest and oldest
    else:
        if int(age) < youngest_age:
            youngest_age = int(age)
            youngest_name = name

        if int(age) > oldest_age:
            oldest_age = int(age)
            oldest_name = name

    # Update values
    people_processed += 1
    total_age += int(age)
    name, age = input("Enter the name and age of the next person: ").split()

# Output results
average = "NaN"
if people_processed != 0:
    average = total_age / people_processed

print(f"The average age is {average}")
print(f"{oldest_name} is the oldest at {oldest_age}")
print(f"{youngest_name} is the youngest at {youngest_age}")