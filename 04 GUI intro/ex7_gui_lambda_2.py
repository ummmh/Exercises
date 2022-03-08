from tkinter import *

root = Tk()


def comment(stuff):
    label_text.set(stuff)


root.minsize(300, 50)
label_text = StringVar()
message = Label(root, textvariable=label_text, font=("Courier", 24, "bold"))
message.pack()

Button(root, text="1", command=lambda: comment(1)).pack()
Button(root, text="2", command=lambda: comment(2)).pack()
Button(root, text="3", command=lambda: comment(3)).pack()
Button(root, text="4", command=lambda: comment(4)).pack()
Button(root, text="5", command=lambda: comment(5)).pack()
Button(root, text="6", command=lambda: comment(6)).pack()

root.mainloop()
