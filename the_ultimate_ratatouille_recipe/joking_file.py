import os
print(os.getcwd())
def setup():
    import os
    os.chdir("the_ultimate_ratatouille_recipe")
    return
setup()
print(os.getcwd())

raise Exception("I am an exception!")

"""
fin = open("data.txt", "r")

from linecache import getline
x = getline("data.txt", 0)
print(x)
print("")
data = fin.readline().split()
print(data)
fin.close()


fin = open("data.txt", "r") #count number of lines
l=0
for i in fin:
    l = l+1
print(l)
"""
