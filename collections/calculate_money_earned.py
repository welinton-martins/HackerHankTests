# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def calculate_money_earned(shoe_sizes, customer_requests):
    # Count the occurrences of each shoe size
    shoe_counter = Counter(shoe_sizes)

    # Initialize the total money earned
    total_money = 0

    # Process each customer request
    for size, price in customer_requests:
        if shoe_counter[size] > 0:
            # If the shoe size is available, decrement the count and add the price to the total money
            shoe_counter[size] -= 1
            total_money += price

    return total_money

# Read the input
num_shoes = int(input().strip())
shoe_sizes = list(map(int, input().strip().split()))
num_customers = int(input().strip())
customer_requests = [tuple(map(int, input().strip().split())) for _ in range(num_customers)]

# Calculate the total money earned
total_money_earned = calculate_money_earned(shoe_sizes, customer_requests)

# Print the result
print(total_money_earned)