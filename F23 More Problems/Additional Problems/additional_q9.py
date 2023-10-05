# Preset values 
months = ["january", "february", "march",
          "april", "may", "june", "july",
          "august", "september", "october",
          "november", "december"]

birthdays = []

# Get birthdays
for i in range(5):
    month = input("Enter a month: ")
    day = input("Enter the day: ")

    birthday = str(months.index(month.lower())) + "." + day
    birthdays.append(float(birthday))
    birthdays.sort()

# Output birthdays
for b in birthdays:
    month_index, day = str(b).split(".")
    print(months[int(month_index)].capitalize(), day)