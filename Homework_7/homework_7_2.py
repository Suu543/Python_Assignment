class Person:

    def __init__(self, name, reg_id, age):
        self.name = name
        self.reg_id = reg_id
        self.age = age

    def __str__(self):
        return f'Person({self.name}, {int(self.reg_id)}, {self.age})'


class Student(Person):

    def __init__(self, name, reg_id, age, st_id, major, gpa):
        Person.__init__(self, name, reg_id, age)
        self.st_id = st_id
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f'Person({self.name}, {int(self.reg_id)}, {int(self.age)}, {int(self.st_id)}, {self.major}, {float(self.gpa)})'


def compareStudent(st1, st2, compare):
    if compare == "st_id":
        if st1.st_id < st2.st_id:
            return True
        else:
            return False
    elif compare == "name":
        if ord(st1.name[0].lower()) < ord(st2.name[0].lower()):
            return True
        else:
            return False
    elif compare == "GPA":
        if st1.gpa > st2.gpa:
            return True
        else:
            return False


def sortStudent(L_st, compare):
    for i in range(0, len(L_st)):
        min_idx = i
        for j in range(i + 1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], compare):
                min_idx = j

        if min_idx != i:
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]


def printStudent(L_st):
    for s in range(len(L_st)):
        print(L_st[s])


if __name__ == "__main__":
    students = [
        Student("Kim", 990101, 21, 12345, "EE", 4.0),
        Student("Lee", 980715, 22, 11234, "ME", 4.2),
        Student("Park", 101225, 20, 10234, "ICE", 4.3),
        Student("Hong", 110315, 19, 13123, "CE", 4.1),
        Student("Yoon", 971005, 23, 11321, "ICE", 4.2),
        Student("Wrong", 100000, 23, 15321, "None", 3.2)
    ]

    print("students before sorting : ")
    printStudent(students)

    sortStudent(students, "name")
    print("\nstudents after sorting by name : ")
    printStudent(students)

    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudent(students)

    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudent(students)
