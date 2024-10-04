#!/bin/python3

import math
import os
import random
import re
import sys

def solve(full_name):
    # Split the input string by spaces, preserving the spaces
    words = full_name.split(' ')

    # Capitalize the first letter of each word and convert the rest to lowercase
    capitalized_words = []
    for word in words:
        if word:  # Ensure the word is not empty
            capitalized_word = word.capitalize()
        else:
            capitalized_word = word  # Preserve empty spaces
        capitalized_words.append(capitalized_word)

    # Join the capitalized words back into a single string with spaces
    capitalized_name = ' '.join(capitalized_words)

    return capitalized_name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
