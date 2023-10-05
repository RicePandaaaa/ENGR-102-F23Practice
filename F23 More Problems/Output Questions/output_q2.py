"""
1 A
4 AA
7 AAAA

Output:
10 AAAAAAAA
"""

n = 1
p = "A"
while n < 10:
    p += p
    n += 3
print(n, p)