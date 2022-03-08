from tkinter import *

root = Tk()
root.geometry("400x250")
root.title("Login")

username_label = Label(text="Username:")
username_label.place(x=30, y=50)
username = Entry()
username.place(x=100, y=50)

email_label = Label(text="Email:")
email_label.place(x=30, y=70)
email = Entry()
email.place(x=100, y=70)

pass_label = Label(text="Password:")
pass_label.place(x=30, y=90)
password = Entry()
password.place(x=100, y=90)

login = Button(text="Login")
login.place(x=230, y=120, width=70)

root.mainloop()
