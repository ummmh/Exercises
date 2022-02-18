# Practice exercise - Bus Company
# 17/02/2022

class Bus:
    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        bus_list.append(self)

    def print_details(self):
        return f"Bus no.: {self.number}\nBus route: {self.route}" \
               f"\nBus driver: {self.driver}\n"


# Main Routine
bus_list = []

bus1 = Bus(2010, "Y", "Greg")
bus2 = Bus(2011, "P", "Joel")
bus3 = Bus(2012, "130", "Kent")

for bus in bus_list:
    print(f"Bus no.: {bus.number}\nBus route: {bus.route}"
          f"\nBus driver: {bus.driver}\n")
