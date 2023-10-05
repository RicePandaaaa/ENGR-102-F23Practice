from math import sqrt, pi

# Area and perimeter of circle
area = pi * 2.59 ** 2
perimeter = 2 * pi * 2.59

print(f"The area of the circle is {area}, and the perimeter of the circle is {perimeter}.")

# Side length (based on area)
print(f"The side length of a square whose area equals the circle's is {sqrt(area)}.")

# Side length (based on perimeter)
print(f"The side length of a square whose perimeter equals the circle's is {perimeter/4}.")