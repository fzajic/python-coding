def setup():
    import os
    os.chdir("the_ultimate_ratatouille_recipe")
    return

def read_data_input(file_name):

    fin = open(file_name, "r")
    data = fin.readline().split()
    return data

    numbers = ""
    for i in range(4):
        numbers = numbers + fin.readline() + ""
    return numbers.split()

setup()
