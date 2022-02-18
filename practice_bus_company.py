# Practice exercise - Bus Company
# 17/02/2022

class Bus:
    bus_list = []

    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        Bus.bus_list.append(self)

    def print_details(self):
        for bus in Bus.bus_list:
            if bus == self:
                print(f"Bus no.: {bus.number}\nBus route: {bus.route}"
                      f"\nBus driver: {bus.driver}\n")


def find_bus(question):
    bus_to_find = input(question)
    for bus in Bus.bus_list:
        if bus_to_find == bus.number:
            return Bus.print_details(bus)
    print(f"Bus {bus_to_find} is not registered in the system yet.")


# Main Routine
bus1 = Bus(2010, "Y", "Greg")
bus2 = Bus(2011, "P", "Joel")
bus3 = Bus(2012, "130", "Kent")

find_bus("Which bus number do you want? (e.g. 2010, 2011, etc.): ")
