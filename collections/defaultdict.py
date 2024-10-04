# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# Read the input
n, m = map(int, input().strip().split())

# Initialize a defaultdict to store the indices of each word in group A
word_indices = defaultdict(list)

# Read the words in group A and store their indices
for i in range(1, n + 1):
    word = input().strip()
    word_indices[word].append(i)

# Read the words in group B and process each word
for _ in range(m):
    word = input().strip()
    if word in word_indices:
        print(' '.join(map(str, word_indices[word])))
    else:
        print(-1)
