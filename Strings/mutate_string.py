def mutate_string(string: str, position: int, character: str) -> str:
    # Use slicing to create a new string with the character replaced
    modified_string = string[:position] + character + string[position + 1:]
    return modified_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)