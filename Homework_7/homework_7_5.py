class Mtrx:

    def __init__(self, name, n_row, n_col, L_data):
        self.name = name
        self.n_row = n_row
        self.n_col = n_col
        self.L_data = L_data

    def printList(self, data):
        print('')

        counter = 0

        for num in data:
            counter += 1
            print(f'{num:2}', end=(" " if counter < self.n_col + 1 else "\n"))
            if counter == 5:
                counter = 0

        return ""

    def __str__(self):
        return self.printList(self.L_data)

    def __add__(self, other):
        result = [0] * len(self.L_data)
        for i in range(0, len(self.L_data)):
            result[i] = self.L_data[i] + other.L_data[i]

        return Mtrx("Add_Result", 4, 4, result)

    def __sub__(self, other):
        result = [0] * len(self.L_data)
        for i in range(0, len(self.L_data)):
            result[i] = self.L_data[i] - other.L_data[i]

        return Mtrx("Sub_Result", 4, 4, result)

    def __mul__(self, other):
        result = [0] * len(self.L_data)
        for i in range(0, len(self.L_data)):
            result[i] = self.L_data[i] * other.L_data[i]

        return Mtrx("Mul_Result", 4, 4, result)


if __name__ == "__main__":
    data_1 = [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25
    ]

    data_2 = [
        1, 0, 0, 0, 0,
        0, 1, 0, 0, 0,
        0, 0, 1, 0, 0,
        0, 0, 0, 1, 0,
        0, 0, 0, 0, 1
    ]

    m1 = Mtrx("M1", 4, 4, data_1)
    print("m1 = ", m1)

    m2 = Mtrx("M2", 4, 4, data_2)
    print("m2 = ", m2)

    m3 = m1 + m2
    print("m3 = m1 + m2 =", m3)

    m4 = m1 - m2
    print("m4 = m1 - m2 =", m4)

    m5 = m1 * m2
    print("m5 = m1 * m2 = ", m5)
