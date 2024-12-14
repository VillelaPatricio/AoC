map = []

def print_map(map):
    print(chr(27) + "[2J")
    for line in map:
        final_line = ""
        for char in line:
            final_line += char
        print(final_line)

with open("input.txt", "r") as file:
    for line in file:
        line_list = []
        for char in line:
            line_list.append(char)
        map.append(line_list)

directions = {"up": (0,-1), "right": (1,0), "down":(0,1), "left": (-1,0)}

current = [48,52]
#current = [48,9]
#current = [2,2]
trail = 1
flag = True
direction = "up"
while current[0] >= 0 and current[1] >= 0:
    #print_map(map)
    try:    
    #print(f"Current location: {current}")
        x,y = directions.get(direction)[0], directions.get(direction)[1]
        # print(direction)
        if map[current[1]+y][current[0]+x] != "#":
            current[0] += directions.get(direction)[0]
            current[1] += directions.get(direction)[1]
            map[current[1]][current[0]] = "X"
            trail += 1
            # print("Free path")
            #print(f"-Trail +1 : {trail}")

        else:
            #print(trail)
            #print(f"-Obstacle detected in {current[1]+y,current[0]+x}")
            if direction == "up":
                direction = "right"
            elif direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "left"
            elif direction == "left":
                direction = "up"
            #print("----------------")
    except:
        print("OUT OF MAP")
        current = [-10,-10]

print_map(map)
print(trail)

num_x = 0

for line in map:
    for char in line:
        if char == "X":
            num_x += 1

print(num_x -1)


