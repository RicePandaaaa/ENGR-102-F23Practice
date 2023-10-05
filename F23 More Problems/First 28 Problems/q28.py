# This question will drive me insane
# Why is there another linear interpolation question

timeData = [0, 37, 58, 125, 150, 200]
heightData = [65, 65, 300, 300, 200, 200]

# Function to interpolate
def interpolate(x0, y0, x1, y1, t):
    slope = (y1 - y0) / (x1 - x0)
    h = slope * (t - x0) + y0

    return h

# Get time
time = float(input("Enter the time: "))

while time < timeData[0] or time > timeData[len(timeData)-1]:
    time = float(input("Enter the time: "))

# Figure out bounds
index = 1
while index < len(timeData) and time > timeData[index]:
    index += 1

l = index - 1
r = index

x0 = timeData[l]
x1 = timeData[r]
y0 = heightData[l]
y1 = heightData[r]

# Output
print(f"At time {time}, the height is {interpolate(x0, y0, x1, y1, time)}")