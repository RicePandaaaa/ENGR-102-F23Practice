# Prompt given bounds
timeData = [0, 37, 58, 125, 150, 200]
heightData = [65, 65, 300, 300, 200, 200]

# Take the time
time = float(input("Enter the time from between 0 and 200 seconds: "))

while time < 0 or time > 200:
    time = float(input("Enter the time from between 0 and 200 seconds: "))

# Function for interpolation
def interpolate(x0, y0, x1, y1, t):
    slope = (y1 - y0) / (x1 - x0)
    h = slope * (t - x0) + y0

    return h

# Figure the bounds
for i in range(len(timeData) - 1):
    if timeData[i] <= time <= timeData[i+1]:
        # Calculate and output
        final_height = interpolate(timeData[i], heightData[i], timeData[i+1], heightData[i+1], time)
        print(f"At time {time}s, the height will be {final_height}m")
        break

