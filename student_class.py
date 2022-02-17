# program order: libraries, classes, function, main routine
# Class - first letter uppercase (camelcase)
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # int 0-100

    # method to return student grade
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    # method to add students to course
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True  # to confirm student added
        return False  # Where student is not added

    def get_average_grade(self):
        pass


# Main routine
# instantiate student objects
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

# instantiate course object
course1 = Course("Computer Science", 2)

# add students to course
course1.add_student(s1)
course1.add_student(s2)

# confirm entry of students
for student in course1.students:
    print(student.name)
