students = []

def add_student(student_id, name):
    student = {
        "id": student_id,
        "name": name,
        "grade": None,
        "course": None
    }
    students.append(student)

    return f"Student {name} added"

def assign_grade(student_id, grade, course):
    for student in students:
        if student["id"] == student_id:
            student["course"] =course
            student["grade"] = grade
            return f"Assigned {course} and {grade} to {student['name']}"
    return "student not found"

def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return "Student not found"    