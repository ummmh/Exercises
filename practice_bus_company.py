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


# Main Routine
bus1 = Bus(2010, "Y", "Greg")
bus2 = Bus(2011, "P", "Joel")
bus3 = Bus(2012, "130", "Kent")

for bus in range(len(Bus.bus_list)):
    Bus.print_details(Bus.bus_list[bus])
