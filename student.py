import random
from course import Course


class Student:

    def __init__(self, student_name, student_class):
        self.student_name = student_name
        self.student_id = random.randint(1000, 10000)
        self.student_class = student_class
        self.student_courses = []
        # self.course = Course

    # def add_course(self, course_name):
    def add_course(self, course):
        # c = self.course
        # if self.student_class == c.course_class:
        if self.student_class == course.course_class:
            for i in self.student_courses:
                if course.course_id == i.course_id:
                    print('course already added')
                    return
            self.student_courses.append(course)
            # self.student_courses.append(course_name)
        else:
            print('invalid course class')

    def student_details(self):
        co = ""
        for course in self.student_courses:
            co = f"{course.course_name}, "
        return "id: " + str(self.student_id) + " -- name: " + self.student_name + " -- class: " + self.student_class + " -- courses: " + co
