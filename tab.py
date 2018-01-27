# tab.py
# automatically add tab

from string import *


def list_min(x):
    min_ = None
    for ptr in x:
        if ptr < min_ or min_ == None:
            min_ = ptr
    return min_


def int_input():
    while(1):
        try:
            print "You should input the number of TAB you want to append..."
            print "It should ba an integer..."
            print "If it is over 0, we append TAB..."
            print "If it is below 0, we delete TAB...\nAnd if there doesn't exist such much TAB, we delete all the TAB..."
            n = input("Please input the integer:\n")
            print
            if(int(n) != n):
                print "Error! We can only allow integer..."
                print
                print "*******************************************************"
                continue
            else:
                return n
        except:
            print "Error! We can only allow integer..."
            print
            print "*******************************************************"
            continue


def read_file():
    while(1):
        file_name = raw_input("Please input the temp file name...\n")
        print
        try:
            fv = open(file_name , 'r')
            line_list = fv.readlines()
            fv.close()
            return (line_list , file_name)
        except:
            print "Error! We cannot find the file in the current folder..."
            print 
            print "********************************************************"
            continue


def main():
    print "This program can append/delete TAB automatically..."
    print "This program uses a temp txt file..."
    print "Copy-paste the codes into the txt file and then go on..."
    print

    info = read_file()
    line_list = info[0]
    file_name = info[1]

    number = int_input()

    new_line_list = []

    count_list = []
    for ptr in line_list:
        count = 0
        index = 0
        for fnd in ptr:
            if fnd == ' ':
                count += 1
            elif fnd == '\t':
                ptr = ptr[:index] + "    " + ptr[index + 1 :]
                count += 4
            else:
                break
            index += 1
        count_list.append(count / 4)

    index = 0
    for ptr in line_list:
        if index == 0:
            pass
        continue
    
    if number > 0:
        for ptr in line_list:
            new_line_list.append(" " * 4 * number + ptr)

    elif number == 0:
        new_line_list = line_list

    else:
        index = 0
        min_count = list_min(count_list)
        if number >= -min_count:
            index = 0
            for ptr in count_list:
                new_line_list.append(line_list[index][4 * (- number) :])
                index += 1
        else:
            for ptr in line_list:
                new_line_list.append(ptr[4 * min_count :])

    fv = open(file_name , "w")
    fv.write("")
    fv.close()

    fv = open(file_name , "a")
    for ptr in new_line_list:
        fv.write(ptr)
    fv.close()

    print "Over.."
    print "Please check your temp file now..."
    




main()
