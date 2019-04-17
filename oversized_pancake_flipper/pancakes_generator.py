import random
number_of_cases = int(input("number of test cases? \n"))
fout = open("pancakes.txt", "w")
s = "+-"
for i in range(number_of_cases):
    passlen = random.randint(0, 10)
    #print(passlen)
    p = ""
    for i in range(passlen):
        p = str(p) + str(random.choice(s))
    fout.write(str(p + "\n"))

fout.close()
