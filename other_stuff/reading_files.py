#Excersice B
import sys
if sys.version_info[0] < 3:
    print("python smaller than 3")

with open("testnumbers", "w") as file:
    for i in range(10):
        file.write("line " + str(i) + "\n")

print("done")
