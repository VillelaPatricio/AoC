xmas_counter = 0
file = []
# def 
with open("input.txt", "r") as input:
    for line in input:
        file.append(line)

#print(file)
print(len(file[0]))

for x, line in enumerate(file):
    print(f"line:{x}")
    for y, char in enumerate(line):
        if char == "X":
            #right
            if (line[y:y+4]) == "XMAS":
                xmas_counter += 1

            #left
            if (line[y-3:y+1]) == "SAMX":
                xmas_counter += 1

            #up
            if x>2 and (file[x-1][y]+file[x-2][y]+file[x-3][y]) == "MAS":
                xmas_counter +=1

            #down
            if x<(len(file)-3) and (file[x+1][y]+file[x+2][y]+file[x+3][y]) == "MAS":
                xmas_counter +=1

            #up right
            if (x>2 and y<138) and (file[x-1][y+1]+file[x-2][y+2]+file[x-3][y+3]) == "MAS":
                xmas_counter +=1

            #up left
            if (x>2 and y>2) and (file[x-1][y-1]+file[x-2][y-2]+file[x-3][y-3]) == "MAS":
                xmas_counter +=1

            #down left
            if (x<(len(file)-3) and y>2) and (file[x+1][y-1]+file[x+2][y-2]+file[x+3][y-3]) == "MAS":
                xmas_counter +=1

            #down right
            if (x<(len(file)-3) and y<138) and (file[x+1][y+1]+file[x+2][y+2]+file[x+3][y+3]) == "MAS":
                xmas_counter +=1

print(xmas_counter)
