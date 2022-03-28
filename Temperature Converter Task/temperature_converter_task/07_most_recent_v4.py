""" Get data from user and store it in list,
then display the most recent three entries nicely

Final version based on Trial 3 - adds break loop and checks for empty list
"""

# Set up empty list
all_calculations = []

# Get five entries of data
get_item = ""
while get_item != "zz":
    get_item = input("Enter an item: ")

    if get_item == "zz":
        break

    all_calculations.append(get_item)

print()

if len(all_calculations) == 0:
    print("Oops - the list is empty!")

else:
    # show that everything made it to the list
    print()
    print("*** FULL LIST ***")
    print(all_calculations)

    # prints all items starting at end of the list
    if len(all_calculations) >= 3:
        print("*** MOST RECENT 3 ***")
        for item in range(0, 3):
            print(all_calculations[len(all_calculations) - item - 1])

    else:
        print("*** ITEMS FROM NEWEST TO OLDEST ***")
        for item in all_calculations:
            print(all_calculations[len(all_calculations)
                                   - all_calculations.index(item) - 1])
