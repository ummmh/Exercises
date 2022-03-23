""" Conversion GUI v1
Basic tkinter template copied from 00_tkinter_template.py and based on the
planning done un Trello (component 2 - slide 16)
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows
import random


class Converter:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "#F5F6FF"  # pale blue

        # Converter Frame
        self.converter_frame = Frame(width=300, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Helvetica", "16", "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # User Instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push one"
                                                  " of the buttons below",
                                             font="Helvetica 10", wrap=250,
                                             justify=LEFT, bg=background_colour
                                             , padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Helvetica 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), #1BA1E2 - blue | #FA6800 - orange
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="to Centigrade",
                                  font="Helvetica 10 bold",
                                  bg="#1BA1E2", fg="white", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="to Fahrenheit",
                                  font="Helvetica 10 bold",
                                  bg="#FA6800", fg="white", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame, font="Helvetica 14",
                                     bg=background_colour, pady=10,
                                     text="Conversion will appear here...")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5), #DAE8FC - light blue
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, text="Calculation"
                                                                  " History",
                                       font=("Helvetica", "14"), bg="#DAE8FC",
                                       padx=5, pady=1)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, text="Help",
                                  font=("Helvetica", "14"), bg="#DAE8FC",
                                  padx=5, pady=1)
        self.help_button.grid(row=0, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter Calculator")
    something = Converter(root)
    root.mainloop()
