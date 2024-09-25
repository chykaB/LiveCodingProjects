# from student_data.student import add_student, assign_grade, students
# # import student_data.student

# def main():
#     add_student(1, "grace")
#     add_student(2, "Henry")

#     assign_grade(1, 3, "math")
#     assign_grade(2, 4, "English")

#     print("List of students: ")
#     for student in students:
#         print(student)


# if __name__ == "__main__":
#     main()


# from student_data.student import add_student, assign_grade, students
# import student_data.student
from student_data import eemployee, sstudent 

def main():
    sstudent.add_student(1, "grace")
    sstudent.add_student(2, "Henry")

    sstudent.assign_grade(1, 3, "math")
    sstudent.assign_grade(2, 4, "English")

    print("List of students: ")
    for student in sstudent.students:
        print(student)

    eemployee.add_employee(1, "Kings")
    print("list of employees: ")
    for employee in eemployee.employees:
        print(employee)

if __name__ == "__main__":
    main()