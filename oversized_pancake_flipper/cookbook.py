def read_pancakes(line):
    """Short summary.

    Parameters
    ----------
    line :
        Number of line from which you want to import.

    Returns
    -------
    List
        List of pancakes.

    """
    fin = open("pancakes.txt", "r")
    for i in range(line):
        pancakes_string = fin.readline()
        pancakes_list = []
        for f in range(len(pancakes_string)-1):
            pancakes_list.append(pancakes_string[f])
    fin.close()
    return pancakes_list

def are_all_happy(pancakes):
    """Return True if all pancakes are happy.

    Parameters
    ----------
    pancakes : List
        List of pancakes.

    Returns
    -------
    Boolean
        Either True of False.

    """
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

def flip_pancakes(pancakes, start_index, flipper_size):
    """Short summary.
    Flips flipper_size pancaks from start_index.
    """
    for index in range(start_index, start_index + flipper_size):
        pancakes[index] = swap(pancakes[index])
    return pancakes

def print_pancakes(pancakes, truth):
    """Print pancakes as a string with either indexes bellow or not.

    Parameters
    ----------
    pancakes : List
        List of pancakes
    truth : Boolean
        True - prints out indexes bellow
        False - prints out just the list.

    """
    s = ""
    for i in pancakes:
        s = s + i
    print(s)
    if truth:
        n = ""
        for i in range(len(s)):
            n = n + str(i)
        print(n)
    return
