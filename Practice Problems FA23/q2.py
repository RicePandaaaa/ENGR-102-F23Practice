"""
Write a Python program to take as input 5 birthdays from 5 users (1 each) and output them in 
chronological order. Dates should be entered with the month and day (not year) in the format 
“June 6” as a single input per user. You may format the output however you like (including 
using numbers for the month instead of words). This is a good problem to practice using 
dictionaries.
"""
# Preset variables
months = ["january", "february", "march", "april",
          "may", "june", "july", "august", "september",
          "october", "november", "december"]
dates = []

# Take the input
for i in range(5):
    # Extract the month and day
    date = input("Enter the birthday: ").split(" ")

    month = date[0]
    day = date[1]

    # Convert to a float
    month_number = months.index(month.lower()) + 1
    day_number = day
    if len(day) == 1:
        day_number = "0" + day

    final_date = float(f"{month_number}.{day_number}")
    dates.append(final_date)

# Get chronological order
dates.sort()

# Output
for date in dates:
    date_str = str(date).split(".")
    month_number = int(date_str[0])
    day_number = date_str[1].ljust(2, "0")

    # Get the month
    month = months[month_number - 1]
    print(month.capitalize(), day_number)
