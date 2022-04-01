""" Builds on 06_converter
Add list to hold calculation history at lines 17-18 and append calculations
to list on lines 127-129
Use this file to generate the list of 7 items for v2
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows
import random


class Converter:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "#F5F6FF"  # pale blue

        # Initialise list to hold calculation history
        self.all_calculations = []

        # Converter Frame
        self.converter_frame = Frame(bg=background_colour, pady=10)
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
                                             font="Helvetica 10", wrap=290,
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
                                  command=lambda: self.temp_convert(-459),
                                  bg="#1BA1E2", fg="white", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="to Fahrenheit",
                                  font="Helvetica 10 bold",
                                  command=lambda: self.temp_convert(-273),
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

    def temp_convert(self, low):
        error = "#ffafaf" # pale pink background for when entry box has errors

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check amount is valid and convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = f"{to_convert}° Celsius is {fahrenheit}° Fahrenheit"

            # Check amount is valid and convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert -32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = f"{to_convert}° Celsius is {celsius}° Fahrenheit"

            else:
                # if input is invalid (e.g. too cold)
                answer = "Too Cold!"
                has_errors = "yes"

            # Display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="black")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add answer to list for history
            if answer != "Too Cold!":
                self.all_calculations.append(answer)
                print(self.all_calculations)

        except ValueError:
            self.converted_label.configure(text="Please enter a number",
                                           fg="red")
            self.to_convert_entry.configure(bg=error)

    # round number
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        return rounded


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter Calculator")
    something = Converter(root)
    root.mainloop()
