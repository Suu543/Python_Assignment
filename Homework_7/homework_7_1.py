class Person:

    def __init__(self, name, reg_id, age):
        self.name = name
        self.reg_id = reg_id
        self.age = age

    def __str__(self):
        return f'Person({self.name}, {int(self.reg_id)}, {int(self.age)})'


def printPersonList(L_persons):
    for p in L_persons:
        print(" ", p)


if __name__ == "__main__":
    persons = [
        Person("Kim", 990101, 21),
        Person("Lee", 980715, 22),
        Person("Park", 101225, 20),
        Person("Hong", 110315, 19),
        Person("Yoon", 971005, 23),
        Person("Wrong", 100000, 350),
    ]

    print("persons : ")
    printPersonList(persons)
