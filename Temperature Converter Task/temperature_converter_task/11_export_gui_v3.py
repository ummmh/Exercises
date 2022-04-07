# Started with 09_history_gui_v5

from tkinter import *
from functools import partial  # To prevent unwanted windows
import re


class Converter:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "#F5F6FF"  # pale blue

        # Initialise list to hold calculation history
        # in later versions, list will be populated with user calculations
        self.all_calc_list = ['0° Fahrenheit is -17.8° Celsius',
                                 '0° Celsius is 32° Fahrenheit',
                                 '40° Celsius is 104° Fahrenheit']
        # self.all_calc_list = []
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

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):
        background = "#F5F6FF"  # pale blue

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # if user press cross at top, closes history and 'releases' button
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
                                  font="helvetica 10 italic bold",
                                  fg="#2C6AC7",  # blue
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
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                  bg="#97BAE8", font="helvetica 14 bold",
                                  command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  bg="#DAE8FC", font="helvetica 14 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):
        print(calc_history)  # fpr testing purposes
        background = "#DAE8FC"  # light blue

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export btn
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                           partner))

        # set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.export_heading = Label(self.export_frame,
                                    text="Export Instructions",
                                    font="helvetica 14 bold", bg=background)
        self.export_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename in the box below and "
                                      "press the Save button to save your "
                                      "calculation history to a text file.",
                                 font="helvetica 10 italic", justify=LEFT,
                                 width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame,
                                 text="If the filename you enter below already"
                                      " exists, it's contents will be replaced"
                                      " with your calculation history.",
                                 font="helvetica 10 bold", justify=LEFT,
                                 fg="#FA6800",  # text is orange
                                 width=30, bg="#FADAC8",  # bg = pale orange
                                 wrap=250, padx=10, pady=10)
        self.export_text.grid(row=2)

        # Filename Entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="helvetica 14", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # error message labels (row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="#FA6800",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel button
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="helvetica 14", bg="#97BAE8",
                                  command=partial(lambda: self.save_history(
                                      partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="helvetica 14", bg="#F5F6FF",
                                    command=partial(self.close_export,
                                                    partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        # regular expression to check file name-can be upper/lower case letters
        valid_char = "[A-Za-z0-9_]"  # numbers or underscores
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue
            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = f"no {letter}'s allowed"
            has_error = "yes"

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":  # describe problem
            # display error message
            self.save_error_label.config(text=f"Invalid filename - {problem}")
            # Change entry box background to orange
            self.filename_entry.config(bg="#FADAC8")
            print()
        else:
            # if there are no errors, generate txt file and then close dialogue
            # add .txt suffix
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter Calculator")
    something = Converter(root)
    root.mainloop()
