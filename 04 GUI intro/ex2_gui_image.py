from tkinter import *

root = Tk()

root.title("Using a label to place an image")

# creating a reference to the image
cat_drawing = PhotoImage(file="wonky cat.png")

# placing the image into the label
image_label = Label(root, image=cat_drawing, bg="white")
image_label.pack()

# adding text below the label
text_label = Label(root, text="cat", font=("Comic Sans MS", 25), bg="white")
text_label.pack(fill=X)

root.mainloop()
