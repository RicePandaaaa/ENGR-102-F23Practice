# Get phone number
phone = input("Enter a phone number: ")

# Numpad dictionary
numpad = {"ABC": 2, "DEF": 3, "GHI": 4,
          "JKL": 5, "MNO": 6, "PQRS": 7,
          "TUV": 8, "WXYZ": 9}
          

# Remove the minus sign
phone = phone[:3] + phone[4:]

"""
# Fancy string way
for char in phone:
    # If it's a number
    if char in "0123456789":
        continue

    else:
        for key in numpad:
            if char.upper() in key:
                phone = phone.replace(char, str(numpad[key]))
"""

# Build the string way
new_phone = ""
for char in phone:
    # If it's a number, add it
    if char in "0123456789":
        new_phone += char

    else:
        # Replace the letter with the number
        for key in numpad:
            if char.upper() in key:
                new_phone += str(numpad[key])

# Format the number
print(f"{new_phone[0:3]}-{new_phone[3:6]}-{new_phone[6:]}")
