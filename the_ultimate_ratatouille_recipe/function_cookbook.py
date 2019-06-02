def setup():
    import os
    if os.getcwd() != r"D:\Coding\python-coding\the_ultimate_ratatouille_recipe":
        os.chdir("the_ultimate_ratatouille_recipe")
        print("changing directorey to: \n", os.getcwd(), "\n", "done... \n")
    else:
        print("directory is already set correctly, no need to change it")
    return

setup()

def file_length(input_file):
    fin = open(input_file, "r")
    l = 0
    for i in fin:
        l = l+1
    fin.close()
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
    fin.close()
    return first_lines, case_lengths

def make_integers(line):
    for i in range(len(line)):                             #return
        line[i] = int(line[i])
    return line

def read_data_input(input_file, case_number):               #return number of line of first information of given case number

    from linecache import getline
    begin_line = first_lines(input_file)[0][case_number-1]  #gets first line of case
    case_length = first_lines(input_file)[1][case_number-1] #gets length of case in number of lines
    data_list = []
    for i in range(begin_line, begin_line + case_length):
        line = getline(input_file, i).split()               #make list of numbers from line
        line = make_integers(line)                          #change strings to integers
        data_list.append(line)
    return data_list

def max(recipe_ingredient_value):
    """Returns maximal value of ingredient:
    Parameters
    ----------
    recipe_ingredient_value:
        number of grmas needed for one serving (according to recipe)

    Returns
    -------
        maximal usable value of ingredient
    """

    recipe_ingredient_value = float(recipe_ingredient_value)
    max = recipe_ingredient_value * 1.1
    return max
pri

def min(recipe_ingredient_value):
    recipe_ingredient_value = float(recipe_ingredient_value)
    min = recipe_ingredient_value * 0.9
    return min

def limit(recipe_ingredient_value, type):
    """Short summary:
    Paramters
    ---------
    recipe_ingredient_value:
        number of grams (value)
    type:
        either max or min, depending on desired output

    Returns
    -------

    """
    recipe_ingredient_value = float(recipe_ingredient_value)
    min = round(recipe_ingredient_value * 0.9, 3)
    max = round(recipe_ingredient_value * 1.1, 3)
    if type == max:
        return max
    elif type == min:
        return min


#print(first_lines("data.txt"))
#print(read_data_input("data.txt",6))

#print(limit(100, max))
