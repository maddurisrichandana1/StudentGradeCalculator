from student import Student
from calculator import calculate_percentage, assign_grade

def main():
    name = input("Enter student name: ")
    subjects = {}
    num_subjects = int(input("Enter number of subjects: "))

    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        marks = int(input(f"Enter marks for {subject} (out of 100): "))
        subjects[subject] = marks

    student = Student(name, subjects)
    percentage = calculate_percentage(student.subjects)
    grade = assign_grade(percentage)

    print("\n--- Student Report ---")
    print(f"Name: {student.name}")
    for subject, marks in student.subjects.items():
        print(f"{subject}: {marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
