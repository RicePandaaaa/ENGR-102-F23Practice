"""
a = True
b = True
c = False
d = False
e = True

Output:
False True
"""

a = True
b = bool('False')
c = 5 > 8
d = a and b and c
e = not a or not (b and c)
print(d, e)