from tkinter import *


class Option:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        options.append(self.display_info())

    def display_info(self):
        return f"{self.name} ${self.price:.2f}"


# Change the label text
def show():
    label.config(text=clicked.get())


# Set up the interface
root = Tk()
root.title("Sandwich filling")
root.geometry("300x110")

# Dropdown menu options
options = []
Option("Cheese", 2.5)
Option("Beef", 3.5)
Option("Chicken", 3)
Option("Egg", 1.5)
Option("Lettuce", 1)

clicked = StringVar()

# Initial menu text - dropdown comes from here
clicked.set("Choose sandwich filling...")

# Send dropdown menu to 'clicked' button above
choice = OptionMenu(root, clicked, *options)  # includes whole options list
choice.pack()

# Create button, to change label text
select_button = Button(root, text="click to confirm", command=show)
select_button.pack()

# Create label to hold the option chosen
label = Label(root, text="Choice will appear here")
label.pack()

exit = Button(root, text="EXIT", command=root.destroy)
exit.pack()

root.mainloop()
