line = 1
rules = {}
prints = []
counter = 0
import math

with open("rules.txt", "r") as file:
    for line in file:
        #rules.append((int(line[0:2]), int(line[3:5])))
        if int(line[0:2]) not in rules:
            rules[int(line[0:2])] = [int(line[3:5])]
        else:
            #print(type(rules.get(int(line[0:2]))))
            (rules.get(int(line[0:2]))).append(int(line[3:5]))

with open("input.txt", "r") as input:
    for line in input:
        prints.append([int(x) for x in line.split(",")])

def checker(manual):    
    print(manual)
    for x,page in enumerate(manual):
        print(f"CHECKING: {page}, index: {x}")
        for y,char in enumerate(manual):
            if char in rules.get(page) and x>y:
                print(f"PAGE {char} BROKE THE SEQUENCE")
                # with open("not_ordered.txt","a") as destiny:
                #     destiny.write(f"{manual}\n")
                return 0
    print("SUCCESS")
    return manual[math.floor(len(manual)/2)]

for manual in prints:
    counter += checker(manual)

print(counter)



