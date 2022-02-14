# Program to compare numbers
# 4/02/2022

def int_checker(question):
    error = "Please input a valid number"
    while True:
        try:
            num = int(input(question))
            return num
        except ValueError:
            return error


# main routine
while True:
    num1 = int_checker("Input a number: ")
    num2 = int_checker("Input a number: ")
    if num1 == 0 or num2 == 0:
        break
    elif num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print("The numbers are equal")
