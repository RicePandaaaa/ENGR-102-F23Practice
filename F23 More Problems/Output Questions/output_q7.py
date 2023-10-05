"""
0 1 4 9 16
Output:
[4, 9, 16]
"""

mylist = []
for i in range(5):
    mylist.append(i ** 2)
print(mylist[-3:])