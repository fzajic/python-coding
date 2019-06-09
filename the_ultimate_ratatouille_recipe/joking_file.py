import os
print(os.getcwd())
def setup():
    import os
    os.chdir("the_ultimate_ratatouille_recipe")
    return
#setup()
print(os.getcwd())




print(os.getcwd() == r"C:\Users\filip\Coding\python-coding\the_ultimate_ratatouille_recipe")





def setup(state):
    """Set enviroment
    Paramters
    ---------
    state:
        Set False or True in order to get printed info into terminal
    """
    import os
    if os.getcwd() != print(os.getcwd() == r"C:\Users\filip\Coding\python-coding\the_ultimate_ratatouille_recipe"):
        os.chdir("the_ultimate_ratatouille_recipe")
        if state == True:
            print("changing directorey to: \n", os.getcwd(), "\n", "done... \n")
    else:
        if state == True:
            print("directory is already set correctly, no need to change it")
    return
setup(True)
