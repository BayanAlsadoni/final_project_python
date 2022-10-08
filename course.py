import random


class Course:

    # course_class = None
    def __init__(self, course_class, course_name):
        self.course_id = random.randint(1000, 10000)
        self.course_class = course_class # A B C
        # globals()["course_class"] = self.course_class
        self.course_name = course_name




