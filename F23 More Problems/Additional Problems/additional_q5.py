# Get scores
homework = 0.4 * float(input("Enter HW grade: "))
exam = 0.6 * float(input("Enter exam grade: "))
bonus = input("Enter Y if outside project was done: ") == "Y"


# Calculate final grade
total = homework + exam
if bonus:
    total += 5

# Calcualte final letter
if total >= 90:
    print("A")
elif total >= 80:
    print("B")
elif total >= 70:
    print("C")
elif total >= 60:
    print("D")
else:
    print("F")
