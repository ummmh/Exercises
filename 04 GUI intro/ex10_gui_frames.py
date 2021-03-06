from tkinter import *

root = Tk()
root.title("Exercise 10")

top_frame = Frame(root)
top_frame.pack()

frame = Frame(top_frame)
frame.pack(side=TOP)

bottom_frame = Frame(root)
bottom_frame.pack()

happy_label = Label(frame, text="Happy")
happy_label.pack(side=LEFT)

dog_label = Label(frame, text="Dog")
dog_label.pack(side=LEFT)

happy_button = Button(top_frame, text="Happy")
happy_button.pack(side=LEFT)

sad_button = Button(top_frame, text="Sad")
sad_button.pack(side=LEFT)

creepy_button = Button(top_frame, text="Creepy")
creepy_button.pack(side=LEFT)

dog_button = Button(bottom_frame, text="Dog")
dog_button.pack(side=LEFT)

clown_button = Button(bottom_frame, text="Clown")
clown_button.pack(side=LEFT)

banana_button = Button(bottom_frame, text="Banana")
banana_button.pack(side=LEFT)

root.mainloop()
