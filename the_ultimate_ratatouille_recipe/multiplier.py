while(False):
    number = int(input("input number pls  "))

    for i in range(11):
        print(number * i)

def setup():
    import os
    os.chdir("the_ultimate_ratatouille_recipe")
    return

setup()
print("Hello")
