def setup(state):
    """Set enviroment
    Paramters
    ---------
    state:
        Set False or True in order to get printed info into terminal
    """
    import os
    if os.getcwd() != r"C:\Users\filip\Coding":
        os.chdir("the_ultimate_ratatouille_recipe")
        if state == True:
            print("changing directorey to: \n", os.getcwd(), "\n", "done... \n")
    else:
        if state == True:
            print("directory is already set correctly, no need to change it")
    return


setup(True)

def file_length(input_file):
    """return number of lines file

    Paramters:
    ----------
    input_file:
        name of data file
    """
    fin = open(input_file, "r")
    l = 0
    for i in fin:
        l = l+1
    fin.close()
    return l

def first_lines(input_file):
    """Return number of first line of each case and length of gap between them

    Paramters:
    ----------
    input_file:
        name of data file
    """
    from linecache import getline
    fin = open(input_file, "r")
    first_lines = []
    case_lengths = []
    current_line = 1
    for i in fin:
        if getline(input_file, current_line) == "":
            break
        # get first number of case that determinimumes its length
        first_number = int(getline(input_file, current_line).split()[0])
        first_lines.append(current_line)  # append another begin line of another case
        number_of_case_lines = 2 + first_number  # get case length
        case_lengths.append(number_of_case_lines)
        current_line = current_line + number_of_case_lines
    fin.close()
    return first_lines, case_lengths


def make_integers(line):
    """Make all components of list integers

    Paramters:
    ----------
    line:
        specific data from line (list)

    """
    for i in range(len(line)):
        line[i] = int(line[i])
    return line


def read_data_input(input_file, case_number):
    """Return formated data of case from data file

    Paramters:
    ----------
    input_file:
        name of data file
    case_number:
        number of case from input_input file, detects specific line automatically (cool right?)

    Returns
    -------
    data_list:
        list of list of each line of case
        example: [[1, 8], [10], [11, 13, 17, 11, 16, 14, 12, 18]]
    """
    from linecache import getline
    begin_line = first_lines(input_file)[0][case_number-1]  # gets first line of case
    # gets length of case in number of lines
    case_length = first_lines(input_file)[1][case_number-1]
    data_list = []
    for i in range(begin_line, begin_line + case_length):
        line = getline(input_file, i).split()  # make list of numbers from line
        line = make_integers(line)  # change strings to integers
        data_list.append(line)
    return data_list


def maximum(recipe_ingredient_value):
    """Returns maximumimal value of ingredient:

    Parameters
    ----------
    recipe_ingredient_value:
        number of grmas needed for one serving (according to recipe)

    Returns
    -------
        maximumimal usable value of ingredient
    """

    recipe_ingredient_value = float(recipe_ingredient_value)
    maximum = recipe_ingredient_value * 1.1
    return maximum


def minimum(recipe_ingredient_value):
    """Returns minimal value of ingredient:

    Parameters
    ----------
    recipe_ingredient_value:
        number of grmas needed for one serving (according to recipe)

    Returns
    -------
        minimal usable value of ingredient
    """
    recipe_ingredient_value = float(recipe_ingredient_value)
    minimum = recipe_ingredient_value * 0.9
    return minimum


def limit(recipe_ingredient_value, type):
    """
    Paramters
    ---------
    recipe_ingredient_value:
        number of grams (value)
    type:
        either maximum or minimum, depending on desired output
    """

    recipe_ingredient_value = float(recipe_ingredient_value)
    minimum = round(recipe_ingredient_value * 0.9, 3)
    maximum = round(recipe_ingredient_value * 1.1, 3)
    #print(maximum, minimum)
    if type == "maximum":
        return maximum
    elif type == "minimum":
        return minimum

"""
print(first_lines("data.txt"))
print(read_data_input("data.txt",6))
print(limit(100, "maximum"))
"""

#print("")
#print(read_data_input("data.txt", 5))
