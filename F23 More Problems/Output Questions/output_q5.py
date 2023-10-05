"""
Output:
Hi Ann
"""

mydict = {'Ann' : 18, 'Bob' : 20, 'Charlie' : 19}
if 'Joe' in mydict:
    print("Joe is here")
elif 'Ann' in mydict:
    print("Hi Ann")
else:
    print("Anyone?")