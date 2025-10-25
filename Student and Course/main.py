from lib.course import Course
from lib.student import Student

cs = Course("Computer Science")
me = Course("Mechanical Engineering")
psy = Course("Psychology")
bbm = Course("Business Management")

student1 = Student("Student1", [cs,bbm])
student2 = Student("Student2", [psy,me])

student1.list_courses()
student2.list_courses()

student1.enroll(psy)

print("\nStudent1 Courses")
student1.list_courses()
