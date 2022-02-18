# Practice exercise - Bus Company
# 17/02/2022

class Bus:
    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver

    def print_details(self):
        return f"Bus no.: {self.number}\nBus route: {self.route}" \
               f"\nBus driver: {self.driver}\n"


# Main Routine
bus1 = Bus(2010, "Y", "Greg")
bus2 = Bus(2011, "P", "Neg")
bus3 = Bus(2012, "130", "Egg")

print(Bus.print_details(bus1))
print(Bus.print_details(bus2))
print(Bus.print_details(bus3))
