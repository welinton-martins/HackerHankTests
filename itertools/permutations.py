from itertools import permutations

# Read the input
input_string, permutation_size = input().strip().split()
permutation_size = int(permutation_size)

# Generate all permutations of the specified size
perms = permutations(input_string, permutation_size)

# Print each permutation on a separate line
for perm in sorted(perms):
    print(''.join(perm))