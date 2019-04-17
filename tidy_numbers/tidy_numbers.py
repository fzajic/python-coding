def is_in_order(numberin):
    number_list = []
    for i in numberin:
        number_list.append(i)
    sorted_number = sorted(number_list)
    if number_list == sorted_number:
        return True
    else:
        return False

#print(in_order(str(input())))      #just a test

def read_line(line):               #read value of particular line of file
    fin = open("file.txt", "r")

    for i in range(line):           #used move to line to be read
        number = fin.readline()
    fin.close
    return number                   #returns the value of the read line

def last_tidy_number(input_line):   #get last tidy number before input number
    limit_number = int(read_line(int(input_line)))
    number = limit_number
    for i in range(limit_number):
        if is_in_order(str(number)):
            return number
        number = limit_number - i
while True:
    print(last_tidy_number(str(input("what line do you want to try? "))))
