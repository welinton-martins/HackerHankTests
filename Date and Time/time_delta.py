#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Define the format string for parsing the timestamps
    fmt = "%a %d %b %Y %H:%M:%S %z"

    # Parse the timestamps including the time zone information
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    # Calculate the absolute difference in seconds
    diff = abs((dt1 - dt2).total_seconds())

    # Return the difference as an integer
    return int(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
