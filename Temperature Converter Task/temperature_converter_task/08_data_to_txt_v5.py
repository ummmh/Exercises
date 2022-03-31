# Source: https://www.quru99.com?reading-and-writing-files-in-python.html

# need to import the regular expression library re
import re

# Data to be outputted
data = ['I', 'love', 'computers']

# get filename, can't be blank /  invalid
# assume valid data for now

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a filename: ")

    # regular expression to check file name-can be upper or lower case letters,
    valid_char = "[A-Za-z0-9_]"  # numbers or underscores
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
        print(f"Invalid filename - {problem}")
        print()
    else:
        print("You entered a valid filename")  # allow valid file name

# add .txt suffix
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

for item in data:
    f.write(item + "\n")

# close file
f.close()
