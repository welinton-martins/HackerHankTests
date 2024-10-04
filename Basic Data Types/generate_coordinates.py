def generate_coordinates(x, y, z, n):
    # Using list comprehension to generate the list of coordinates
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    return coordinates

# Example usage:
if __name__ == "__main__":
    x = int(input().strip())
    y = int(input().strip())
    z = int(input().strip())
    n = int(input().strip())

    result = generate_coordinates(x, y, z, n)
    print(result)
