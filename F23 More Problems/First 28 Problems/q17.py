xdata = [0, 1, 2, 3, 4]

# Store the results
y_data = []

# Function to solve for y
def y(x):
    return (4.12 * x**2) + (1.52 * x) - 7.1

# Calculate y
for x in xdata:
    y_data.append(y(x))

print(y_data)