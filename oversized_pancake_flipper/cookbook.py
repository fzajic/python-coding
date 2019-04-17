def read_pancakes(line):
    fin = open("pancakes.txt", "r")
    for i in range(line):
        pancakes_string = fin.readline()
        pancakes_list = []
        for f in range(len(pancakes_string)-1):
            pancakes_list.append(pancakes_string[f])
    fin.close()
    return pancakes_list

def are_all_happy(pancakes):
    sample = []
    for i in range(len(pancakes)):
        sample.append("+")
    if sample == pancakes:
        return True
    else:
        return False

def swap(element): #swap - for +, or vice versa
    if element == "+": return "-"
    else: return"+"

def flip_pancakes(pancakes, start_index):
    for index in range(start_index, start_index + flipper_size):
        pancakes[index] = swap(pancakes[index])
    return pancakes

def print_pancakes(pancakes):
    s = ""
    for i in pancakes:
        s = s + i
    print(s)
    n = ""
    for i in range(len(s)):
        n = n + str(i)
    print(n)
    return
