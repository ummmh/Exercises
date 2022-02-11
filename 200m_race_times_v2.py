"""Program that asks for the finishing times in either the 100m, 200m or 400m
race, and allows the viewer to see all the times entered, fastest time,
the average time, as well as clearing all the times."
Created by Janna Lei Eugenio
11/02/2022 - version 2
"""


# functions
def select_options(list, race):
    while True:
        print(f"\n{race}m RACE:")
        print("--------OPTIONS--------\n1. Add race times\n2. See Times, "
              "fastest time, & average time\n3. Clear race times")
        try:
            selection = int(input("Select an option (or -1 to quit): "))
            if selection == 1:
                add_time(list)
            elif selection == 2:
                print_totals(list, race)
            elif selection == 3:
                print("\n--------OPTION 3--------")
                list.clear()
                print(f"List for {race}m cleared")
            elif selection == -1:
                print()
                break
            else:
                print("Please select a valid option\n")
                continue
        except ValueError:
            print("Please select a valid option\n")


def add_time(list):
    print("\n--------OPTION 1--------")
    while True:
        try:
            time = float(input("Enter finishing time (input -1 to exit): "))
            if time == -1:
                break
            list.append(time)
        except ValueError:
            print("Please enter a valid race time\n")
    return list


def print_totals(list, race):
    print("\n--------OPTION 2--------")
    try:
        print(f"Race times entered for {race}m:")
        for race_time in list:
            print(race_time)
        print()
        list.sort()
        print(f"The fastest time was {list[0]}")
        average_time = sum(list) / len(list)
        print(f"The average time was {average_time}")
    except IndexError:
        print("There are no finishing times inputted yet!")


# main routine
# variables
hundred_metre = []
two_hundred_metre = []
four_hundred_metre = []

while True:
    try:
        race = int(input("Please select a race (100, 200, 400) or -1 to exit: "
                         ))
        if race == 100:
            select_options(hundred_metre, race)
        elif race == 200:
            select_options(two_hundred_metre, race)
        elif race == 400:
            select_options(four_hundred_metre, race)
        elif race == -1:
            break
        else:
            print("Please select a valid option\n")
    except ValueError:
        print("Please select a valid option\n")

print("\nGoodbye!")
