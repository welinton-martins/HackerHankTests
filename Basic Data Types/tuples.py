
if __name__ == '__main__':

    # Read the number of elements
    n = int(input())

    # Read the space-separated integers and create a tuple
    elements = map(int, input().split())

    result = tuple(elements)

    # Print the result
    print(hash(result));

    