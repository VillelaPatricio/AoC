xmas_counter = 0
file = []
with open("input.txt", "r") as input:
    for line in input:
        file.append(line)

for y, line in enumerate(file):
    print(f"line:{y}")
    for x, char in enumerate(line):
        if char == "A":
            try:
                if ((file[y-1][x-1]+file[y-1][x+1]) == "SS") and ((file[y+1][x-1]+file[y+1][x+1]) == "MM"):
                    xmas_counter += 1

                elif ((file[y-1][x-1]+file[y-1][x+1]) == "SM") and ((file[y+1][x-1]+file[y+1][x+1]) == "SM"):
                    xmas_counter += 1

                elif ((file[y-1][x-1]+file[y-1][x+1]) == "MS") and ((file[y+1][x-1]+file[y+1][x+1]) == "MS"):
                    xmas_counter += 1

                elif ((file[y-1][x-1]+file[y-1][x+1]) == "MM") and ((file[y+1][x-1]+file[y+1][x+1]) == "SS"):
                    xmas_counter += 1

            except:
                print(f"This A is in corners, position {x+1,y+1}")
print(xmas_counter)