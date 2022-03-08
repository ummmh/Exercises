from tkinter import *

root = Tk()


def comment(stuff):
    label_text.set(stuff)


root.minsize(300, 50)
text = StringVar

Button(root, text="OK", command=lambda: comment("No it's not")).pack()
Button(root, text="Close", command=lambda: comment("Are you sure?")).pack()
Button(root, text="Exit",
       command=lambda: comment("Ha ha - you are trapped!")).pack()

label_text = StringVar()
message = Label(root, textvariable=label_text, font=("Courier", 24, "bold"))
message.pack()

root.mainloop()
