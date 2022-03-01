# Student system
# 24/02/2022

# Classes
class Student:
    def __init__(self, name, age, phone, form_class, subjects, is_male):
        self.name = name
        self.age = age
        self.phone = phone
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = is_male
        self.enrolled = True
        student_list.append(self)

    def student_info(self):
        print("------------------------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone no.: {self.phone}")
        print(f"Form class: {self.form_class}")
        print(f"Subjects: {self.subjects}")
        if self.is_male:
            print(f"{self.name} is male")
        else:
            print(f"{self.name} is female")
        print(f"Enrolled: {self.enrolled}")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        teacher_list.append(self)

    def teacher_info(self):
        print("------------------------------")
        print(f"Name: {self.name}")
        print(f"Class: {self.subject}")


# Functions
def generate_students():
    # available form classes are: "BAKER", "MORGAN", "MCNICOL", "GRAHAM", "BELL", "NIMMO", "BARKER"
    # available classes are: "ART", "ENG", "MAT", "GRA", "DTC", "PHY", "BIO"
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)


# prints the students details
def print_student_details():
    for student in student_list:
        student.student_info()


# asks for an age then prints all students info that age or older
def select_student_age():
    students_older = []
    while True:
        try:
            age = int(input("Enter an age: "))
            for student in student_list:
                if student.age >= age:
                    student.student_info()
                    if student.age > age:
                        students_older.append(student)
            print(f"\nTotal students above the age of {age}: "
                  f"{len(students_older)}")
            return
        except ValueError:
            print("That is not a valid age\n")


# counts the students in a class
def count_students():
    students_in_course = []
    course_teacher = ()
    course = input("What class are you looking for? ").upper()
    for student in student_list:
        if course in student.subjects:
            students_in_course.append(student)
    for teacher in teacher_list:
        if course in teacher.subject:
            course_teacher = teacher.name
    if len(students_in_course) == 0:
        print(f"Sorry there are no students enrolled in {course}")
    else:
        print(f"{course} teacher: {course_teacher}")
        print(f"No. of students in {course}: {len(students_in_course)}")


# finds a student and print their information
def find_student():
    student_to_find = input("Enter name of the student: ").title()
    for student in student_list:
        if student.name == student_to_find:
            student.student_info()
            return student
    print("Sorry, no student was found with that name")
    return None


# Adds a new student
def add_student():
    name = input("Enter the new student's name: ").title()
    while True:
        try:
            age = int(input("Enter the new student's age: "))
            break
        except ValueError:
            print("Please enter a valid age")
    phone = input("Enter the new student's phone number: ")
    form_class = input("Enter the new student's form class: ")
    subjects = input("Enter the new student's subjects: ").upper()
    gender = input("Enter the new student's gender (M or F): ").upper()
    if gender == "M":
        is_male = True
    else:
        is_male = False
    Student(name, age, phone, form_class, subjects, is_male)
    print(name, "has been added to the user list")


# deletes a student from list
def remove_student():
    student = find_student()
    while True:
        confirm = input("\nAre you sure you want to remove this student? "
                        "(Y or N): ").upper()
        if confirm == "Y":
            print(f"{student.name} has been removed from the roll")
            student_list.remove(student)
            return
        elif confirm == "N":
            print(f"{student.name} has not been removed from the roll")
            return
        else:
            print("Please input either 'Y' or 'N'")


# find students of a certain gender
def select_student_gender():
    students = []
    while True:
        gender = input("Input gender (M or F): ").upper()
        if gender == "M":
            for student in student_list:
                if student.is_male:
                    students.append(student)
                    student.student_info()
            print(f"\nTotal male students: {len(students)}")
            return
        elif gender == "F":
            for student in student_list:
                if not student.is_male:
                    students.append(student)
                    student.student_info()
            print(f"\nTotal female students: {len(students)}")
            return
        else:
            print("Please enter M or F\n")


# prints the teachers details
def print_teacher_details():
    for teacher in teacher_list:
        teacher.teacher_info()


# main menu
def menu():
    while True:
        print("***** MAIN MENU *****")
        print("\n1. Count students taking a particular subject")
        print("2. Print a full list of all students")
        print("3. Print a list of students above a particular age")
        print("4. Print a list of students a particular gender")
        print("5. Get the details of a particular student")
        print("6. Add a new student")
        print("7. Remove a student from roll")
        print("8. Print a full list of all teachers")

        choice = input("\nWhat would you like to do?\n- Enter one of the options"
                       " or 'Q' to exit: ").upper()
        if choice == "1":
            print("\n***COUNT STUDENTS IN A SUBJECT***")
            count_students()
            print()
        elif choice == "2":
            print("\n***LIST OF ALL STUDENTS***")
            print_student_details()
            print()
        elif choice == "3":
            print("\n***LIST OF STUDENTS ABOVE A PARTICULAR AGE***")
            select_student_age()
            print()
        elif choice == "4":
            print("\n***LIST OF STUDENTS A PARTICULAR GENDER***")
            select_student_gender()
            print()
        elif choice == "5":
            print("\n***SHOW DETAILS OF A SPECIFIC STUDENT***")
            find_student()
            print()
        elif choice == "6":
            print("\n***ADD A STUDENT***")
            add_student()
            print()
        elif choice == "7":
            print("\n***REMOVE A STUDENT***")
            remove_student()
            print()
        elif choice == "8":
            print("\n***LIST OF ALL TEACHERS**")
            print_teacher_details()
            print()
        elif choice == "Q":
            print("\nGoodbye!")
            break
        else:
            print()
            print("---Please select a valid option or 'Q' to quit---")
            print()


# Main Routine
# lists
student_list = []
teacher_list = []

# generating the students
generate_students()

# Teachers
Teacher("Baker", "GRA")
Teacher("Barker", "MAT")
Teacher("Graham", "BIO")
Teacher("Morgan", "DTC")
Teacher("Bell", "PHY")
Teacher("Nimmo", "ART")
Teacher("McNicol", "ENG")

# Main menu function
menu()
