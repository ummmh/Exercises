# program order: libraries, classes, function, main routine
# Class - first letter uppercase (camelcase)
class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def print_details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}."

    def change_age(self, age):
        self.age = age


# Main routine
dog1 = Dog("Spot", 7, "black")
dog2 = Dog("Jazz", 5, "white")

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

# Change the age function called
dog1.change_age(17)
dog2.change_age(9)

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
