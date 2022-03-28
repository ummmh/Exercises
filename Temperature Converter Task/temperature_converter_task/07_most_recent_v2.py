""" Get data from user and store it in list, then display the most recent three
entries nicely
Trial 2 - uses a deque method (no need for reverse ordering)
"""

from collections import deque
calculations = deque()

# Get five entries of data
for item in range(0, 5):
    get_item = input("Enter an item: ")

    # add item to start of list
    calculations.appendleft(get_item)


# show that everything made it to the list
print()
print("*** FULL LIST ***")
print(calculations)

print()

print("*** MOST RECENT 3 ***")
for item in range(0, 3):
    print(calculations[item])
