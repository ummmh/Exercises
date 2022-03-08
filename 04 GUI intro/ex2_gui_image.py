from tkinter import *

root = Tk()

root.title("Using a label to place an image")

# creating a reference to the image
cat_drawing = PhotoImage(file="wonky cat.png")

# placing the image into the label
image_label = Label(root, image=cat_drawing)
image_label.pack()

# adding text below the label
text_label = Label(root, text="cat", font=("Comic Sans MS", 25))
text_label.pack()

root.mainloop()
