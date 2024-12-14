rules = {}
prints = []
counter = 0
import math
import sys

sys.setrecursionlimit(10**7)

def checker(manual, number):    
    print(f"Unsortedlsit {number+1}: {manual}")

    for x,page in enumerate(manual):
        #print(f"CHECKING: {page}, index: {x}")
        for y,char in enumerate(manual):
            if char in rules.get(page) and x>y:
                #print(f"PAGE {char} BROKE THE SEQUENCE")
                #print(f"Nor working list: {manual}")
                sub_list = manual.copy()
                change = sub_list.pop(y)
                sub_list = sub_list[:x] + [change] + sub_list[x:]
                #print(f"List to test: {sub_list}")
                return checker(sub_list, number)

    print(f"SUCCESS, ordered list: {manual}")
    #return manual
    return manual[math.floor(len(manual)/2)]

with open("rules.txt", "r") as file:
    for line in file:
        #rules.append((int(line[0:2]), int(line[3:5])))
        if int(line[0:2]) not in rules:
            rules[int(line[0:2])] = [int(line[3:5])]
        else:
            #print(type(rules.get(int(line[0:2]))))
            (rules.get(int(line[0:2]))).append(int(line[3:5]))

with open("not_ordered.txt", "r") as input:
    for line in input:
        prints.append([int(x) for x in line[1:-2].split(", ")])

for number,manual in enumerate(prints):
    counter += checker(manual, number)

print(counter)

