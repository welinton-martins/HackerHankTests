import calendar

# Read the input
month, day, year = map(int, input().strip().split())

# Determine the day of the week
day_index = calendar.weekday(year, month, day)

# Map the day index to the day name
day_names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
day_name = day_names[day_index]

# Print the day name in uppercase
print(day_name)
