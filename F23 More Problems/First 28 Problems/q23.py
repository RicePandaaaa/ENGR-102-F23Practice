"""
x = 3
y = 4

first if is false, skip to else
first inner if is true

Output:
D
G
"""

x = 3
y = 4
if x%2 == 0:
    if y>3:
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