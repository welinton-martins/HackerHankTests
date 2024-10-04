def merge_the_tools(string, k):
    # Calculate the number of substrings
    num_substrings = len(string) // k

    for i in range(num_substrings):
        # Extract the substring of length k
        substring = string[i * k:(i + 1) * k]

        # Create a unique subsequence
        unique_subsequence = ''
        seen_chars = set()

        for char in substring:
            if char not in seen_chars:
                unique_subsequence += char
                seen_chars.add(char)

        # Print the unique subsequence
        print(unique_subsequence)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k