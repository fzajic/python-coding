def read_data_input(file_name):
    fin = open(file_name, "r")
    data = []
    for i in range(4):
        data.append(fin.readlines())
    fin.close()
    return data


print(read_data_input("input_data.txt"))
