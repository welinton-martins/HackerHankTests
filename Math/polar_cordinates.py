import cmath

# Read the input
complex_number_str = input().strip()

# Convert the input string to a complex number
complex_number = complex(complex_number_str)

# Calculate the modulus (absolute value) of the complex number
modulus = abs(complex_number)

# Calculate the phase (argument) of the complex number
phase = cmath.phase(complex_number)

# Print the modulus and phase, formatted to three decimal places
print(f"{modulus:.3f}")
print(f"{phase:.3f}")