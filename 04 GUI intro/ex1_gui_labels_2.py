from tkinter import *

root = Tk()

root.title("Exercise 1")
computer = Label(root, bg="lime", fg="white", text="computer",
                 font=("Times", 50, "italic"))
computer.pack()

science = Label(root, bg="blue", fg="yellow", text="science is",
                font=("Comic Sans MS", 50, "bold"))
science.pack()

awesome = Label(root, bg="orange", fg="red", text="awesome!",
                font=("Arial Black", 50))
awesome.pack()

root.mainloop()
