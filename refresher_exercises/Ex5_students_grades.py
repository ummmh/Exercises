# Program to keep track of students marks and grades
# 14/02/2022

def calc_uni_grade(grade):
    if grade >= 90:
        letter = "A+"
    elif grade >= 85:
        letter = "A"
    elif grade >= 80:
        letter = "A-"
    elif grade >= 75:
        letter = "B+"
    elif grade >= 70:
        letter = "B"
    elif grade >= 65:
        letter = "B-"
    elif grade >= 60:
        letter = "C+"
    elif grade >= 55:
        letter = "C"
    elif grade >= 50:
        letter = "C-"
    elif grade >= 40:
        letter = "D"
    else:
        letter = "E"
    return letter


grade_list = []

while True:
    student_name = input("Student's name (input 'x' to exit): ").title()
    if student_name == "X":
        break
    try:
        student_grade = int(input("Grade: "))
        if student_grade in range(0, 101):
            uni_grade = calc_uni_grade(student_grade)
            grade_list.append([student_name, student_grade, uni_grade])
            print()
        else:
            print("Please put a grade between 0 - 100\n")
            continue
    except ValueError:
        print("Please put a grade between 0 - 100\n")

best_grade = sorted(grade_list, key=lambda row: row[1])
average_grade = sum(x[1] for x in grade_list) / len(grade_list)

print("\nStudent grades:")
for item in grade_list:
    print(f"{item[0]}: {item[2]} ({item[1]}%)")
print(f"\nStudent with the highest grade: {best_grade[-1][0]}: "
      f"{best_grade[-1][2]} ({best_grade[-1][1]}%)")
print(f"Average student grade: {average_grade}")
