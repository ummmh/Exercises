from tkinter import *
root = Tk()

# changing the title of the window
root.title("My first window")

# window .geometry - to set size of 600px wide x 200px tall
root.geometry("600x200")  # string using 'x not '*' - no spaces either side
root.maxsize(800, 400)  # int values - sets max resizable dimensions

# adding a label widget
greeting = Label(text="Hello, Tkinter")

# need to use .pack( to show the object in the root
greeting.pack()

root.mainloop()
