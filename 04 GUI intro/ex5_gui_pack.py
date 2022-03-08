from tkinter import *

root = Tk()

root.title("Exercise 5")
root.geometry("600x400")

red = Label(root, bg="red", fg="white", text="Red")
red.pack(fill=Y, side=LEFT)

green = Label(root, bg="lime", text="Green")
green.pack(fill=X, side=BOTTOM)

blue = Label(root, bg="blue", fg="white", text="Blue")
blue.pack(fill=BOTH, padx=30, pady=30, ipady=200)

root.mainloop()
