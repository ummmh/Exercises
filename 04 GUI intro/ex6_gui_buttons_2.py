from tkinter import *


def count_up():
    global number
    number += 1
    print(number)
    return number


def count_down():
    global number
    number -= 1
    print(number)
    return number


root = Tk()
root.title("My first button")
root.minsize(200, 100)

up = Button(root, text="Count up", command=count_up).pack()
down = Button(root, text="Count down", command=count_down).pack()

number = 0
print(number)

root.mainloop()
