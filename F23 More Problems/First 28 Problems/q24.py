"""
0 -> 11: 0 1 2 3 4 5 6 7 8 9 10
Must be even and divisble by 3

Output:
0
6
"""

for i in range(12):
    if i%2!=1 and i%3==0:
        print(i)