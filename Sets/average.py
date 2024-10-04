def average(array):
    # Convert the array to a set to eliminate duplicates
    distinct_heights = set(arr)

    # Calculate the sum of the distinct heights
    total_sum = sum(distinct_heights)

    # Calculate the number of distinct heights
    num_distinct = len(distinct_heights)

    # Calculate the average
    avg = total_sum / num_distinct

    # Return the average rounded to three decimal places
    return round(avg, 3)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result