def is_leap(year):
    leap = False
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, check if it is divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
    return leap

year = int(input())
print(is_leap(year))