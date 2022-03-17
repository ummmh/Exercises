from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "#F5F6FF"

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

        # Help button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Helvetica", "14"), bg="#DAE8FC",
                                  padx=5, pady=1, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):
        background = "#DAE8FC"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

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
                                  command=self.close_help)
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter Calculator")
    something = Converter(root)
    root.mainloop()
