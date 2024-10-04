def split_and_join(line: str) -> str:
    # Split the string on spaces
    words = line.split(" ")
    # Join the list of words with hyphens
    result = "-".join(words)
    return result


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result