""" Get data from user and store it in list,
then display the most recent three entries nicely

Trial 3 - prints list in reverse order
(no need for extra code or importing extra libraries)
"""

# Set up empty list
all_calculations = []

# Get five entries of data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

all_calculations.reverse()

# show that everything made it to the list
print()
print("*** FULL LIST ***")
print(all_calculations)

print()

print("*** MOST RECENT 3 ***")
# prints all items starting at end of the list
for item in range(0, 3):
    print(all_calculations[len(all_calculations) - item - 1])
