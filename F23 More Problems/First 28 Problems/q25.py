"""
Output:
2 A
4 AA
16 AAAA
256
AAAAAAAA
"""

x = 2
y = "A"
while x<100:
    print(x, y)
    x *= x
    y += y
print(x)
print(y)