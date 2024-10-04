# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# Read the input lists
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

# Compute the Cartesian product
cartesian_product = list(product(A, B))

# Print the Cartesian product in the required format
for tuple in cartesian_product:
    print(tuple, end=' ')