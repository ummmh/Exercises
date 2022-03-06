from tkinter import *
root = Tk()

root.title("Welcome")
welcome = Label(root, bg="black", fg="white", text="Welcome",
                font=("Times", 50, "bold"))

welcome.pack()

root.mainloop()
