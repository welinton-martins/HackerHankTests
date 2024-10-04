def calculate_average_marks():
    # Read the number of student records
    n = int(input().strip())
    
    # Initialize a dictionary to store student names and their marks
    student_marks = {}
    
    # Read each student's name and marks
    for _ in range(n):
        line = input().strip().split()
        name = line[0]
        # Convert the remaining items in the list to floats and store in dictionary
        marks = list(map(float, line[1:]))
        student_marks[name] = marks
    
    # Read the query name
    query_name = input().strip()
    
    # Calculate the average marks for the queried student
    if query_name in student_marks:
        average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
        # Print the average rounded to two decimal places
        print(f"{average_marks:.2f}")

if __name__ == "__main__":
    calculate_average_marks()
