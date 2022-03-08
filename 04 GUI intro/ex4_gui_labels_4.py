from tkinter import *

root = Tk()

root.title("Exercise 4")
computer = Label(root, bg="lime", fg="white", text="computer",
                 font=("Times", 50, "italic"))
computer.pack(fill=X, side=LEFT)

science = Label(root, bg="blue", fg="yellow", text="science is",
                font=("Comic Sans MS", 50, "bold"))
science.pack(fill=X, side=RIGHT)

awesome = Label(root, bg="orange", fg="red", text="awesome!",
                font=("Arial Black", 50))
awesome.pack(fill=X, side=RIGHT)

root.mainloop()
