from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Exercise 14")

btn_relwidth = Button(root, bg="lime", text="relwidth=0.2")
btn_relwidth.place(relwidth=0.2)

btn_relx = Button(root, bg="magenta", text="relx=0.3")
btn_relx.place(relx=0.3)

btn_x = Button(root, bg="cyan", text="x=400px")
btn_x.place(x=400)

btn_y = Button(root, bg="cyan", text="y=321")
btn_y.place(y=321)

btn_x_y_relheight = Button(root, bg="lime", text="x=100, y=50, relheight=0.6")
btn_x_y_relheight.place(x=100, y=50, relheight=0.6)

btn_heightxy = Button(root, bg="red", text="height=150, x=200, y=200")
btn_heightxy.place(height=150, x=200, y=200)

btn_rely = Button(root, bg="magenta", text="relx=0.8")
btn_rely.place(rely=0.8)

btn_widthxy = Button(root, bg="red", text="width=150, x=300, y=400")
btn_widthxy.place(width=150, x=300, y=400)

root.mainloop()
