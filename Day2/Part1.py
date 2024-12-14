import operator
lista = []
counter = 0

with open ("Data.txt", "r") as file:
    for i in file:
        lista.append([int(i) for i in (i.split())])

def gen_checker(list):
    direction = None

    if list[0] < list[1]:
        direction = operator.lt
    elif list[0] > list[1]:
        direction = operator.gt
    else:
        return 0

    i = 0
    while i < (len(list)-1):
        if direction(list[i],list[i+1]) and (abs(list[i] - list[i+1]) < 4):
            i+=1 
        else:
            return 0
    return 1

for list in lista:
    counter += gen_checker(list)

print(counter)

