def calculate_percentage(subjects):
    total_marks = sum(subjects.values())
    max_marks = len(subjects) * 100
    percentage = (total_marks / max_marks) * 100
    return percentage

def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
