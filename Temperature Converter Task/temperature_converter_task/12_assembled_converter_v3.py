# Started with 09_history_gui_v5

from tkinter import *
from functools import partial  # To prevent unwanted windows
import re


class Converter:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "#F5F6FF"  # pale blue

        # Initialise list to hold calculation history
        self.all_calc_list = []

        # Converter Frame
        self.converter_frame = Frame(bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font="Helvetica 16 bold",
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # User Instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push one"
                                                  " of the buttons below",
                                             font="Helvetica 10", wrap=290,
                                             justify=LEFT,
                                             bg=background_colour,
                                             padx=10, pady=10)
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

        self.history_button = Button(self.hist_help_frame,
                                     text="Calculation History",
                                     font="Helvetica 14", bg="#DAE8FC",
                                     width=15, command=lambda:
                                     self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, text="Help",
                                  font="Helvetica 14", bg="#DAE8FC",
                                  padx=5, pady=1, command=self.help)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        error = "#ffafaf"  # pale pink background for when entry box has errors

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
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = f"{to_convert}° Fahrenheit is {celsius}° Celsius"

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
            if has_errors == "no":
                self.all_calc_list.append(answer)
                self.history_button.config(state=NORMAL)

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

    def history(self, calc_history):
        History(self, calc_history)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a  number in the box "
                                          "and then push on of the buttons to "
                                          "convert the number to either "
                                          "degrees Celsius or degrees "
                                          "Fahrenheit.\n\nThe Calculation "
                                          "History area shows up to seven "
                                          "recent calculations with the most "
                                          "recent at the top.\n\nYou can also "
                                          "export your full calculation "
                                          "history to a text file if desired.",
                                     font="helvetica 10")


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
                history_string += calc_history[
                                      len(calc_history) - item - 1] + "\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(
                                                   item) - 1] + "\n"
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
        # print(calc_history)  # for testing purposes
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
        # print(filename)

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


class Help:
    def __init__(self, partner):
        background = "#DAE8FC"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                           partner))

        # set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.help_heading = Label(self.help_frame, text="Help / Instructions",
                                  font="helvetica 14 bold", bg=background)
        self.help_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="#F5F6FF", font="helvetica 14 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter Calculator")
    something = Converter(root)
    root.mainloop()
