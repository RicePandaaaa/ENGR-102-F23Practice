"""
x = 2
y = "A"

Output:
2 A
4 AA
16 AAAA
"""

x = 2
y = "A"
while x<100:
    print(x, y)
    x *= x
    y += y