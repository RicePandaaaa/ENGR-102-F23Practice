"""
a = 1
b = 2
c = 'a'
d = 3

first condition is false
second condition is false

Answer: Yellow

"""

a = 1
b = 2
c = 'a'
d = int(float('3.14'))
if a == 1 and d == 3.14:
    print('Green')
elif c == a or d > 3:
    print('Red')
else:
    print('Yellow')