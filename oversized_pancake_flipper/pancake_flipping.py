from cookbook import read_pancakes, are_all_happy, flip_pancakes, print_pancakes

flipper_size = 3#input("what is size of the flipper? \n")

pancakes = read_pancakes(18)

print_pancakes(pancakes)
counter = 0
for i in pancakes:
    if i == "_":
        pancakes = flip_pancakes(pancakes, counter)
    counter = counter + 1
print(pancakes)
