# Get input
phone_number = input("Enter your phone number: ")

# Preset values
pad = {"ABC": 2, "DEF": 3, "GHI": 4, "JKL": 5,
       "MNO": 6, "PQRS": 7, "TUV": 8, "WXYZ": 9}

# Make new phone number
combined_number = "".join(phone_number.split("-"))
new_number = ""

for i in range(len(combined_number)):
    # Extract character
    char = combined_number[i]

    # If is a number, add to new number directly
    if char.isnumeric():
        new_number += char

    # Else, check in dictionary
    else:
        for char_set in pad.keys():
            if char.upper() in char_set:
                new_number += str(pad[char_set])

# Reformat new number
print(f"{new_number[:3]}-{new_number[3:6]}-{new_number[6:]}")