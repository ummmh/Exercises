# Source: https://www.quru99.com?reading-and-writing-files-in-python.html

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# get filename, can't be blank /  invalid
# assume valid data for now
filename = input("Enter a filename: ")

# create file to hold data
f = open(filename, "w+")

for item in data:
    f.write(item)

# close file
f.close()
