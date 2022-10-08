import random

from course import Course
from student import Student

students_list = []
courses_list = []


def course_class():
    while True:
        class_course = input('select class course(A, B, C):')
        if class_course in ['A', 'B', 'C']:
            break
    return class_course


def get_all_students(students):
    for st in students:
        print(st.student_details())


def find_std(student_id,students):
    for sdt in students:
        if sdt.student_id == student_id:
            return std
    return -1


def find_course(course_name, courses):
    for cr in courses:
        if cr.course_name == course_name:
            return cr
    return -1


while True:
    choice = int(input("""
select choice please:
1. add new student
2. remove student
3. edit student
4. display all students
5. create new course
6. add course to student
0. exit
write the select here 💁🏻‍ =>"""))

    if choice == 1:
        std_name = input('enter student name:')
        std = Student(std_name, course_class())
        for s in students_list:
            if std.student_id == s.student_id:
                std.student_id = random.randint(1000, 10000)
        students_list.append(std)
        print('student added successfully')
        print(std.student_details())

    if choice == 2:
        get_all_students(students_list)
        std_id = int(input('enter user id'))
        student = find_std(std_id,students_list)
        if student == -1:
            print('student not exist')
        else:
            students_list.remove(student)
            print('student deleted successfully')

    if choice == 3:
        get_all_students(students_list)

        std_id = int(input('enter student id'))

        std = find_std(std_id,students_list)
        if std == -1 :
            print('student not exist')
        else:
            std_name = input('enter student name')
            std.student_class = course_class()
            std.student_name = std_name
            print('student editing successfully')
            std.student_details()

    if choice == 4:
        for st in students_list:
            print(st.student_details())

    if choice == 5:
        c_name = input('enter course name')
        c = Course(course_class(), c_name)
        for cr in courses_list:
            if c.course_id == cr.course_id:
                c.course_id = random.randint(1000, 10000)
        courses_list.append(c)
        print('course created successfully')
        print(f"id: {c.course_id} -- name: {c.course_name} -- class: {c.course_class}")

    if choice == 6:
        std_num = int(input('enter student number'))
        std = find_std(std_num, students_list)
        if std == -1:
            print('student not exist')
        else:
            course_name = input('enter course name:')
            cr = find_course(course_name,courses_list)
            if cr == -1:
                print('course not exist')
            else:
                std.add_course(cr)
                print(f'course: {course_name} added successfully to student: {std.student_name}')

    if choice == 0:
        break

    if choice not in [0, 1, 2, 3, 4, 5, 6]:
        print('you enter error number❗')

