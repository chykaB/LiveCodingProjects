employees = []

def add_employee(employee_id, name):
    student = {
        "id": employee_id,
        "name": name,
        "grade": None,
        "course": None
    }
    employees.append(student)

    return f"Student {name} added"