# Enter your code here. Read input from STDIN. Print output to STDOUT
def perform_division(a, b):
    try:
        # Attempt to perform integer division
        result = a // b
        print(result)
    except ZeroDivisionError as e:
        # Handle division by zero
        print(f"Error Code: {e}")
    except ValueError as e:
        # Handle invalid literal for int()
        print(f"Error Code: {e}")

# Read the input
num_test_cases = int(input().strip())

# Process each test case
for _ in range(num_test_cases):
    a, b = input().strip().split()
    try:
        # Convert inputs to integers
        a = int(a)
        b = int(b)
        perform_division(a, b)
    except ValueError as e:
        # Handle invalid literal for int() during conversion
        print(f"Error Code: {e}")
