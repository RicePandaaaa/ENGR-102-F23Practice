"""
Output:
The fox jumped down
"""

mystr = 'The quick brown fox jumped over the lazy dog'
print(mystr[:3], end=' ')
if mystr[4] == 'q':
    if 'fox' in mystr:
        print('fox', end=' ')
    else:
        print('dog', end=' ')
    if mystr[-5] != 'z':
        print('jumped', end=' ')
    else:
        print('hopped', end=' ')
elif 'x' in mystr:
    if 'white' in mystr:
        print('white mouse', end=' ')
    else:
        print('brown cow', end=' ')
    if 'y' not in mystr:
        print('sat', end=' ')
    else:
        print('dropped', end=' ')
else:
    print(mystr[4:26], end=' ')
print('down')