from Part1 import gen_checker

lista = []
counter = 0

with open ("Data.txt", "r") as file:
    for i in file:
        lista.append([int(i) for i in (i.split())])

for list in lista:
    print(f"Working on list: {list}")
    if gen_checker(list) == True:
        print("ORIGINALWORKED")
        counter += 1

    else:
        sub_i = 0
        while sub_i < len(list):
            sub_list = [x for j,x in enumerate(list) if j != (sub_i)]
            print(f"ORINAL LIST FAILED, CHECKING {sub_list}")
            if gen_checker(sub_list) == True:
                counter += 1
                sub_i = len(list)
                print(f"SUBLIST {sub_list} WAS SUCCESSFUL")
            else:
                sub_i += 1

print(counter)
