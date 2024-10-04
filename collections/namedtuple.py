# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

# Read the input
n = int(input().strip())
columns = input().strip().split()

# Create a named tuple for the student data
Student = namedtuple('Student', columns)

# Read the student data and store it in a list of named tuples
students = [Student(*input().strip().split()) for _ in range(n)]

# Calculate the average marks and print the result
average_marks = sum(int(student.MARKS) for student in students) / n
print(f"{average_marks:.2f}")
