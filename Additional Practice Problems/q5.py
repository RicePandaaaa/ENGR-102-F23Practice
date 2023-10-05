from math import pi, sqrt

# Take input
area = float(input("Enter an area: "))

# Area of circle = pi * r**2
radius = sqrt(area / pi)

# Area of square = s**2
side_length = sqrt(area)

# Output
print(f"A circle with area {area:.1f} has radius: {radius:.1f}")
print(f"A square with area {area:.1f} has side length: {side_length:.1f}")
