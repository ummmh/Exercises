# This is a re-purposed copy of 01_help_gui_v5

from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "#F5F6FF"  # pale blue

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

        # Export button (row 1)
        self.export_button = Button(self.converter_frame, text="Export",
                                  font=("Helvetica", "14"), bg="#97BAE8",  # dark blue
                                  padx=5, pady=1, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)


class Export:
    def __init__(self, partner):
        background = "#DAE8FC"  # light blue

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export button
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
                                 width=40, bg="#FADAC8",  # background is pale orange
                                 wrap=250, padx=10, pady=10)
        self.export_text.grid(row=2)

        # Filename Entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="helvetica 14", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save / Cancel frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=4, pady=10)

        # Save and Cancel button
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="helvetica 14", bg="#97BAE8")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="helvetica 14", bg="#F5F6FF",
                                    command=partial(self.close_export,
                                                    partner))
        self.cancel_button.grid(row=0, column=1)

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
