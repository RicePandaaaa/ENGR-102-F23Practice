"""
Write a Python program to take as input 5 birthdays from 5 users (1 each) and output them in 
chronological order. Dates should be entered with the month and day (not year) in the format 
“June 6” as a single input per user. You may format the output however you like (including 
using numbers for the month instead of words). This is a good problem to practice using 
dictionaries.
"""
# Preset variables
months = {"january": 1, "february": 2, "march": 3, "april": 4,
          "may": 5, "june": 6, "july": 7, "august": 8, "september": 9,
          "october": 10, "november": 11, "december": 12}
dates = []

# Take the input
for i in range(5):
    # Extract the month and day
    date_str = input("Enter the birthday: ")
    date = date_str.split(" ")

    month = date[0]
    day = date[1]

    # Insert if first date
    if len(dates) == 0:
        dates.append(date_str)
        continue

    # Order the dates
    for j in range(len(dates)):
        # Extract the date to compare
        indexed_date = dates[j].split(" ")
        i_month = indexed_date[0]
        i_day = indexed_date[1]

        # Check the month
        if months[month.lower()] < months[i_month.lower()]:
            dates = dates[:j] + [date_str] + dates[j:]
            break

        elif months[month.lower()] == months[i_month.lower()]:
            # Same month, check day
            if int(day) <= int(i_day):
                dates = dates[:j] + [date_str] + dates[j:]
                break

    # Date is the last in line
    else:
        dates.append(date_str)

# Output the dates
print(", ".join(dates))
            
        

