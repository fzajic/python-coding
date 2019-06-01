def setup():
    import os
    os.chdir("the_ultimate_ratatouille_recipe")
    return
setup()


def file_length(input_file):
    fin = open(input_file, "r")
    l = 0
    for i in fin:
        l = l+1
    return l

def first_lines(input_file):
    from linecache import getline
    fin = open(input_file, "r")
    first_lines = []
    case_lengths = []
    current_line = 1
    for i in fin:
        if getline(input_file, current_line) == "":
            break
        first_number = int(getline(input_file, current_line).split()[0])    #get first number of case that determines its length
        first_lines.append(current_line)                                    #append another begin line of another case
        number_of_case_lines = 2 + first_number                             #get case length
        case_lengths.append(number_of_case_lines)
        current_line = current_line + number_of_case_lines
    return first_lines, case_lengths

def make_integers(line):
    for i in range(len(line)):
        #print(i)
        line[i] = int(line[i])
    return line

def read_data_input(input_file, case_number):               #return number of line of first information of given case number
    from linecache import getline
    begin_line = first_lines(input_file)[0][case_number-1]  #gets first line of case
    case_length = first_lines(input_file)[1][case_number-1] #gets length of case in number of lines
    for i in range(begin_line, begin_line + case_length):
        line = getline(input_file, i).split()               #make list of numbers from line
        line = make_integers(line)                          #change strings to integers
        print(line)
    return

def max(recipe_value):
    recipe_value = float(recipe_value)
    max = recipe_value * 1.1
    return max

def min(recipe_value):
    recipe_value = float(recipe_value)
    min = recipe_value * 0.9
    return min

def limit(recipe_value):
    recipe_value = float(recipe_value)
    min = recipe_value * 0.9
    max = recipe_value * 1.1
    return min, max
    



#print(first_lines("data.txt"))
print(read_data_input("data.txt",6))
