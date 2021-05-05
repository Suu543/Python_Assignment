def extract_Demo(file_name):
    demography_file = open(f'{file_name}', 'r')
    demo_list = []

    for demo_data in demography_file.readlines():
        name, capital, population, area = demo_data.split()
        tmp = (name, capital, int(population), int(area))
        demo_list.append(tmp)

    demography_file.close()
    return demo_list


def print_data_sorted_by_population(demo_data):
    idx = 0
    print("List of countries: ")

    for data in demo_data:
        print(f'Country[ {idx}] : {data}')
        idx = idx + 1

    idx = 0
    print("\nList of countries sorted by demography(number of people): ")
    sorted_data = sorted(demo_data, key=lambda data: data[2], reverse=True)

    for data in sorted_data:
        print(f'Country[ {idx}] : {data}')
        idx = idx + 1


extractedData = extract_Demo('demography.txt')
print_data_sorted_by_population(extractedData)
