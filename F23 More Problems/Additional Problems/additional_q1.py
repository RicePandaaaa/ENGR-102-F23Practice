# Data storage
masses = []
volumes = []

mass = 1
# Get input while mass is non zero
while mass > 0:
    try:
        print("-------------------")
        mass = float(input("Enter a mass: "))
        volume = float(input("Enter a volume: "))
    except:
        mass = 1
        continue
    else:
        if mass == 0:
            break

        if volume == 0 or mass < 0:
            continue
        
        print(f"M: {mass} and V: {volume} added!")
        masses.append(mass)
        volumes.append(volume)

# Calculate densities
densities = []

for i in range(len(masses)):
    densities.append(masses[i] / volumes[i])

print(densities)

