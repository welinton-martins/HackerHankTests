def count_substring(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    
    # Loop through the string
    for i in range(len(string) - substring_length + 1):
        # Check if the substring matches the part of the string
        if string[i:i + substring_length] == substring:
            count += 1
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)