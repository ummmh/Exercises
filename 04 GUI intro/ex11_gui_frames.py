from tkinter import *

root = Tk()
root.title("Exercise 11")
root.geometry("300x300")

frame = Frame(root)
frame.pack()

happy_label = Label(frame, text="Happy").grid(sticky=N)

dog_label = Label(frame, text="Dog").grid(sticky=N)

happy_button = Button(frame, text="Happy").grid(sticky=W, ipadx=10)

sad_button = Button(frame, text="Sad").grid(ipadx=10)

creepy_button = Button(frame, text="Creepy").grid(sticky=E, ipadx=10)

dog_button = Button(frame, text="Dog").grid(sticky=SW, ipadx=10)

clown_button = Button(frame, text="Clown").grid(sticky=S, ipadx=10)

banana_button = Button(frame, text="Banana").grid(sticky=SE, ipadx=10)

root.mainloop()
