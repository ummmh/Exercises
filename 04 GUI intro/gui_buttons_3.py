from tkinter import *
root = Tk()


def press_button():
    text = entry_text.get()
    label_text.set(text)


root.title("Changing label text")
root.minsize(300, 50)

entry_text = StringVar()
enter_something = Entry(textvariable=entry_text, font=("Times", 15))
enter_something.pack()

button = Button(root, text="Press to show message", command=press_button)
button.pack()

label_text = StringVar()
message = Label(root, textvariable=label_text, font=("Courier", 24, "bold"))
message.pack()

root.mainloop()
