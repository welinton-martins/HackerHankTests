import math

# Read the input
AB = int(input().strip())
BC = int(input().strip())

# Calculate the angle in radians
theta_radians = math.atan(AB / BC)

# Convert the angle to degrees
theta_degrees = math.degrees(theta_radians)

# Round the angle to the nearest integer
theta_rounded = round(theta_degrees)

# Print the result with the degree symbol
print(f"{theta_rounded}\u00B0")
