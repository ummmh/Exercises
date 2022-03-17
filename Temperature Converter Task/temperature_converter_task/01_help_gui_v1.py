from tkinter import *
import random


class Converter:
    def __init__(self, parent):
        print("hello world")

        # Formatting variables
        background_colour = "#F5F6FF"

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300,
                                     bg=background_colour)
        self.converter_frame.grid()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter Calculator")
    something = Converter(root)
    root.mainloop()
