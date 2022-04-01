""" Follows on from 09_history_gui_v4,py
- Changed the name of "all calculations" list to "all_calc_list"
- Changed class name history to History
- Changed the command on history to lambda
- Then (again) changed the history function
- Add calc_history parameter to History class
"""

from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "#F5F6FF"  # pale blue

        # Initialise list to hold calculation history
        # in later versions, list will be populated with user calculations
        self.all_calc_list = ['0° Fahrenheit is -17.8° Celsius',
                                 '0° Celsius is 32° Fahrenheit',
                                 '40° Celsius is 104° Fahrenheit']

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300,
                                     bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Helvetica", "16", "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                  font=("Helvetica", "14"), bg="#DAE8FC",
                                  padx=5, pady=1,
                                     command=lambda: self.history
                                     (self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):
        background = "#F5F6FF"  # pale blue

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # if users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(
            self.close_history, partner))

        # set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # set up history heading (row 0)
        self.history_heading = Label(self.history_frame,
                                     text="Calculation History",
                                     font="helvetica 14 bold", bg=background)
        self.history_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent "
                                       "calculations. Please use the export "
                                       "button to create a text file of all "
                                       "your calculations for this session.",
                                  font="helvetica 10 italic bold", fg="#2C6AC7",  # blue
                                  justify=LEFT, bg=background, wrap=250,
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # History output (row 2)
        history_string = ""
        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)-item-1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item)-1]+"\n"
                self.history_text.config(text="Here is your calculation "
                                              "history. You can use the export"
                                              " button to save this data to a"
                                              " text file if desired.")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="helvetica 11",
                                justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Export",
                                  bg="#DAE8FC", font="helvetica 14 bold")
        self.dismiss_btn.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  bg="#DAE8FC", font="helvetica 14 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter Calculator")
    something = Converter(root)
    root.mainloop()
