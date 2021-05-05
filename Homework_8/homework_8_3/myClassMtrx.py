class MyMtrx:
    def __init__(self, name, num_rows, num_cols, list_data):
        self.name = name
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.list_data = list_data

    def __add__(self, other):
        result = [len(other.list_data[0]) * [0]
                  for i in range(len(other.list_data))]
        for i in range(0, len(other.list_data)):
            for j in range(0, len(other.list_data)):
                result[i][j] = self.list_data[i][j] + other.list_data[i][j]

        return result

    def __sub__(self, other):
        result = [len(other.list_data[0]) * [0]
                  for i in range(len(other.list_data))]
        for i in range(0, len(other.list_data)):
            for j in range(0, len(other.list_data)):
                result[i][j] = self.list_data[i][j] - other.list_data[i][j]

        return result

    def __mul__(self, other):
        result = [len(other.list_data[0]) * [0]
                  for i in range(len(other.list_data))]
        for i in range(0, len(other.list_data)):
            for j in range(0, len(other.list_data)):
                result[i][j] = self.list_data[i][j] * other.list_data[i][j]

        return result


def read_matrix_txt(file_name):
    matrix_file = open(f'{file_name}', 'r')
    matrix_list = []

    for line in matrix_file.readlines():
        matrix_list.append([float(x) for x in line.split()])

    return matrix_list


def build_matrix(matrix_data):
    mA = MyMtrx('mA', int(matrix_data[0][0]), int(
        matrix_data[0][1]), matrix_data[1:6])
    mB = MyMtrx('mB', int(matrix_data[6][0]), int(
        matrix_data[6][1]), matrix_data[7:])

    return [mA, mB]


def print_result(matrix_data):
    for data in matrix_data:
        print(f"n_row = {data.num_rows}, n_col = {data.num_cols}")
        print(f'{data.name} = ')
        print_matrix(data.list_data)

    print(f"mC = {matrix_data[0].name} + {matrix_data[1].name}")
    print_matrix(matrix_data[0] + matrix_data[1])

    print(f"mD = {matrix_data[0].name} - {matrix_data[1].name}")
    print_matrix(matrix_data[0] - matrix_data[1])

    print(f"mE = {matrix_data[0].name} * {matrix_data[1].name}")
    print_matrix(matrix_data[0] * matrix_data[1])


def print_matrix(list_data):
    for matrix in list_data:
        counter = 0
        for elem in matrix:
            counter += 1
            print(f"{elem:4}", end=(" " if counter < len(matrix) else "\n"))


matrix_data = read_matrix_txt('matrix_data.txt')
print_result(build_matrix(matrix_data))
