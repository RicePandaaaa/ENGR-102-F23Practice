"""
x = 10
y = 5

first if is true, first else is ignored

Output:
B
C
G
H
"""

x = 10
y = 5
if x%2 == 0:
    if y>5:
        print("A")
    else:
        print("B")
        print("C")
else:
    if y<5:
        print("D")
    else:
        print("E")
        print("F")
print("G")
print("H")