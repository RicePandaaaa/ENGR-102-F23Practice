"""
Output:

The answer is... A True 124
"""

a = 5
b = 'b'
c = True
print("The answer is...", end=' ')
if a != 10:
    print("A", end=' ')
elif b == 'b':
    print("B", end=' ')
else:
    print("C", end=' ')
z = c and bool(a)
print(z, end=' ')
d = a ** 3 + 25 % 3 - 12 // 5
print(d)
