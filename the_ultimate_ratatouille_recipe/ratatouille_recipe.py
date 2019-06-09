import os
print(os.getcwd())
#os.chdir(r"the_ultimate_ratatouille_recipe")
from function_cookbook import setup, read_data_input, maximum, minimum
#setup(False)
print(read_data_input("data.txt", 5))
setup(True)
