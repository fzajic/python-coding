def setup():
    import os
    os.chdir("the_ultimate_ratatouille_recipe")
    return

#setup()



fin = open("input_data.txt", "r")

from linecache import getline
x = getline("input_data.txt", 0)
print(x)
print("")
data = fin.readline().split()
print(data)
fin.close()


fin = open("input_data.txt", "r") #count number of lines
l=0
for i in fin:
    l = l+1
print(l)
