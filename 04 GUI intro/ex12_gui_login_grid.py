from tkinter import *

root = Tk()
root.title("Login")

username_label = Label(text="Username:")
username_label.grid(column=0, row=0)
username = Entry()
username.grid(column=1, row=0)

email_label = Label(text="Email:")
email_label.grid(column=0, row=1)
email = Entry()
email.grid(column=1, row=1)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=2)
password = Entry()
password.grid(column=1, row=2)

login = Button(text="Login")
login.grid(column=2, row=3, ipadx=10)

root.mainloop()
