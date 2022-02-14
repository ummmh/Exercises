# program order: libraries, classes, function, main routine
# Class - first letter uppercase (camelcase)
class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def print_details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}."


# Main routine
dog1 = Dog("Spot", 7, "black")
dog2 = Dog("Jazz", 5, "white")

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
