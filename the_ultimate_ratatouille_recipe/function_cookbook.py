def read_data_input(file_name):
    fin = open(file_name, "r")
    data = fin.readline().split()
    return data

print(read_data_input("input_data.txt"))
