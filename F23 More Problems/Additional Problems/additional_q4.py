# Get input
name = input("Enter your name: ")
scores = input("Enter your scores separated by spaces: ").split(" ")

# Calcualte average
total = 0
for score in scores:
    total += float(score)

print(f"Hi {name}, your exam average is {total / len(scores)}")