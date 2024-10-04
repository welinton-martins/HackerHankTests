def find_students_with_second_lowest_grade():
    # Read the number of students
    n = int(input().strip())
    
    # Initialize a list to hold students and their grades
    students = []
    
    # Read student names and grades
    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])
    
    # Extract grades and find the unique grades sorted
    grades = sorted(set(grade for name, grade in students))
    
    # The second lowest grade is the one we need
    second_lowest_grade = grades[1]  # second lowest will be at index 1
    
    # Find names of students with the second lowest grade
    names_with_second_lowest = sorted([name for name, grade in students if grade == second_lowest_grade])
    
    # Print each name on a new line
    for name in names_with_second_lowest:
        print(name)

# Example usage:
if __name__ == "__main__":
    find_students_with_second_lowest_grade()
