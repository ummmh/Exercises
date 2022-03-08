from tkinter import *

root = Tk()


def change(number):
    if number == 7:
        current.set(current.get()*7)
    elif number == 3:
        current.set(current.get()+3)
    elif number == 2:
        current.set(current.get()-2)
    elif number == 0:
        current.set(current.get()*0)


root.title("Puzzle number buttons")
current = IntVar()
goal = IntVar()

current.set(0)
goal.set(71)
Label(root, textvariable=current, bg="blue", fg="white", font=("Arial", 24)).pack(side=LEFT)

Button(root, text="x7", font=("Arial", 24, "bold"), command=lambda: change(7)).pack(side=LEFT)
Button(root, text="+3", font=("Arial", 24, "bold"), command=lambda: change(3)).pack(side=LEFT)
Button(root, text="-2", font=("Arial", 24, "bold"), command=lambda: change(2)).pack(side=LEFT)
Button(root, text="0", font=("Arial", 24, "bold"), command=lambda: change(0)).pack(side=LEFT)

Label(root, textvariable=goal, bg="blue", fg="white", font=("Arial", 24)).pack(side=LEFT)

root.mainloop()
