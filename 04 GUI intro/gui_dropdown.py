from tkinter import *


# Change the label text
def show():
    label.config(text=f"You chose {clicked.get()}")


# Set up the interface
root = Tk()
root.title("Dropdown menu")
root.geometry("300x90")

# Dropdown menu options
options = ["Cheese", "Beef", "Chicken", "Egg", "Lettuce", "Tomato", "Avocado"]

clicked = StringVar()

# Initial menu text - dropdown comes from here
clicked.set("Choose filling...")

# Send dropdown menu to 'clicked' button above
choice = OptionMenu(root, clicked, *options)  # includes whole options list
choice.pack()

# Create button, to change label text
select_button = Button(root, text="click to confirm", command=show)
select_button.pack()

# Create label to hold the option chosen
label = Label(root, text="Choice will appear here")
label.pack()

root.mainloop()
