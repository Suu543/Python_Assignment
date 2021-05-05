from array import *
from datetime import *
import random
import time
import os
import json
import pickle


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


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return {'__datetime__': o.replace(microsecond=0).isoformat()}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}


def main():
    matrix_data = read_matrix_txt('matrix_data.txt')
    print_result(build_matrix(matrix_data))
    # print(build_matrix(matrix_data)[0])

    mA = build_matrix(matrix_data)[0]

    mA_json = open("mA_json.txt", "w")
    json.dump(mA, mA_json, indent=4, cls=CustomEncoder)
    mA_json.close()
    mA_json_size = os.path.getsize("mA_json.txt")

    mA_bin = open("mA_pickle.bin", 'wb')
    pickle.dump(mA, mA_bin)
    mA_bin.close()
    mA_bin_size = os.path.getsize("mA_pickle.bin")

    print("size of mA_json.txt = ", mA_json_size)
    print("size of mA_pickle.bin = ", mA_bin_size)


if __name__ == "__main__":
    print("Executing main()")
    main()

    print('''
    - JSON은 텍스트 직렬화 형식인 반면, Pickle은 바이너리 직렬화 형식입니다.
    - JSON은 사람이 읽을 수 있지만, Pickle은 그렇지 않습니다.
    - JSON은 상호 운용이 가능하고, 파이썬 생태계 외부에서 널리 사용되지만, Pickle은 파이썬에서만 사용할 수 있습니다.
    - JSON은 기본적으로 파이썬 내장형 일부만 표시할 수 있지만, 사용자 정의 클래스는 표시하지 못합니다.
    - Pickle은 파이썬 언어에서 사용하는 대부분의 데이터 형을 나타낼 수 있습니다.
    - Pickle과 달리, 신뢰할 수 없는 JSON의 역 질려화는 그 자체로 임의 코드 실행 취약점을 만들지 않습니다.
    - JSON 형식의 데이터와, Pickle 형식의 데이터 크기가 다른 이유는, JSON 파일의 데이터 값을 불러올 때 변환하는 과정에서 형식을 변환시키는 데 시간이 만이 소요되지마느
      Pickle은 리스트나, 클래스 같은 텍스트가 아닌 자료형을 컴퓨터가 이해할 수 있는 기계어로 변환해 저장하기 때문에 더 적은 크기를 가집니다.
      요약하자면, JSON은 변환할 수 있는 것 없는 것을 구분하고, 또 그것을 인간이 읽을 수 있는 방식으로 변환해야하기 때문에, 시간도 조금 더 걸리고, 크기가 큽니다.
      반면에, Pickle의 경우 구분하는 데 시간을 할애하지 않아도 되고, 또한 기계가 이해할 수 있는 이진수로 바로 변환하기 때문에 더 적은 시간과, 작은 크기를 보입니다.
    ''')
