def extract_student_records(file_name):
    students_file = open(f'{file_name}', 'r')
    students_list = []

    for student in students_file.readlines():
        name, kor, eng, math, sci = student.split()
        tmp = (name, int(kor), int(eng), int(math), int(sci))
        students_list.append(tmp)

    students_file.close()
    return students_list


def calculate_scores(records):
    print("After calculate_scores(students)")
    print(f"name   kor eng math sci sum avg")

    for record in records:
        print(
            f"{record[0]:5}: {record[1]:2}, {record[2]:2}, {record[3]:3}, {record[4]:2}, {sum(record[1:5]):1} {sum(record[1:5]) / 4}")


extracted_data = extract_student_records('student_records.txt')
calculate_scores(extracted_data)
