def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0

    # Iterate over each starting position in the string
    for i in range(len(string)):
        # Check if the current character is a vowel or consonant
        if string[i] in vowels:
            # If it's a vowel, Kevin gets points for all substrings starting from this position
            kevin_score += len(string) - i
        else:
            # If it's a consonant, Stuart gets points for all substrings starting from this position
            stuart_score += len(string) - i

    # Determine the winner
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)