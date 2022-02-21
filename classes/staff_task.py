#
# 18/02/2022

class AllStaff:
    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job

    def show(self):
        print(f"{self.id}: {self.name} - age: {self.age} birthdate: "
              f"{self.birthdate} job title: {self.job}")


class Management(AllStaff):
    def __init__(self, name, age, id, birthdate, job, car):
        super().__init__(self, name, age, id, birthdate, job)
        self.car = car

    def show(self):
        print(f"{self.id}: {self.name} - age: {self.age} birthdate: "
              f"{self.birthdate} job title: {self.job} car: {self.car}")


class Clerical(AllStaff):
    def __init__(self, name, age, id, birthdate, job, typing_speed):
        super().__init__(self, name, age, id, birthdate, job)
        self.typing_speed = typing_speed

    def show(self):
        print(f"{self.id}: {self.name} - age: {self.age} birthdate: "
              f"{self.birthdate} job title: {self.job} typing speed: "
              f"{self.typing_speed}")


class Factory(AllStaff):
    pass

# main routine

