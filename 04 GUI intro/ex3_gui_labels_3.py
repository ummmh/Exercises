from tkinter import *

root = Tk()

root.title("Exercise 3")
computer = Label(root, bg="lime", fg="white", text="computer",
                 font=("Times", 50, "italic"))
computer.pack(fill=X)

science = Label(root, bg="blue", fg="yellow", text="science is",
                font=("Comic Sans MS", 50, "bold"))
science.pack(fill=X)

awesome = Label(root, bg="orange", fg="red", text="awesome!",
                font=("Arial Black", 50))
awesome.pack(fill=X)

root.mainloop()
