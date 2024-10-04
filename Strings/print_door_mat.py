# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_door_mat(X, Y):
    # Ensure X is odd and Y is 3 times X
    if X % 2 == 0 or Y != 3 * X:
        print("Invalid dimensions")
        return

    # Top part of the mat
    for i in range(X // 2):
        line = '.|.' * (2 * i + 1)
        print(line.center(Y, '-'))

    # Middle part of the mat
    print('WELCOME'.center(Y, '-'))

    # Bottom part of the mat
    for i in range(X // 2 - 1, -1, -1):
        line = '.|.' * (2 * i + 1)
        print(line.center(Y, '-'))

# Example usage
X, Y = map(int, input().split())
print_door_mat(X, Y)