"""
I have no idea what \\b does tbh (oh it takes out the last character)

Output: 
Howdy Texas A&M Engineering students!
"""

mystr = "Howdy! Welcome to Texas A&M Engineering!"
print(mystr[:5] + mystr[6] + mystr[18:] + '\b students!')