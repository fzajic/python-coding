from cookbook import read_pancakes, are_all_happy, flip_pancakes, print_pancakes

flipper_size = 4#input("what is size of the flipper? \n")

pancakes = read_pancakes(18)
counter = 0
times_flipped = 0
for i in pancakes:
    if counter <= len(pancakes) - flipper_size:
        if i == "-":
            pancakes = flip_pancakes(pancakes, counter, flipper_size)
            times_flipped = times_flipped + 1
    counter = counter + 1
if are_all_happy(pancakes):
    print(str(times_flipped) + " times flipped")
else:
    print("impossible")
