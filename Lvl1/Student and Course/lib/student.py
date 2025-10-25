from .course import Course
class Student:
    def __init__(self, name: str, courses: list["Course"]):#
        self.name = name
        self.courses = courses

    def enroll(self, course: Course):
        if not isinstance(course, Course):
            raise Exception("Only Course instances can be added.")
        self.courses.append(course)


    def list_courses(self):
        for course in self.courses:
            print(course)