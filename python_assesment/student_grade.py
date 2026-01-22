# student_grades.py
# Student Grade Management System
# Demonstrates dictionaries, lists, functions, loops, and formatted output

# Function to calculate average grade
def calculate_average(grades_list):
    return sum(grades_list) / len(grades_list)


# Function to determine letter grade
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Function to display student report
def display_student_report(student):
    average = calculate_average(student["grades"])
    letter_grade = get_letter_grade(average)

    print(f"Student Name: {student['name']}")
    print(f"Email: {student['email']}")
    print(f"Grades: {student['grades']}")
    print(f"Average Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print("-" * 40)


# Create student dictionaries
student1 = {
    "name": "Alice Tan",
    "grades": [88, 92, 85, 90],
    "email": "alice.tan@email.com"
}

student2 = {
    "name": "Brian Lee",
    "grades": [75, 80, 78, 82],
    "email": "brian.lee@email.com"
}

student3 = {
    "name": "Catherine Wong",
    "grades": [91, 94, 89, 96],
    "email": "catherine.wong@email.com"
}

# Store all students in a list
students = [student1, student2, student3]

# Display reports for all students
print("STUDENT REPORTS\n")
for student in students:
    display_student_report(student)

# Find the student with the highest average
top_student = max(students, key=lambda s: calculate_average(s["grades"]))
top_average = calculate_average(top_student["grades"])

print("Top Performing Student:")
print(f"{top_student['name']} with an average of {top_average:.2f}")