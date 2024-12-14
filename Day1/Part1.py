from sorting import sorting

file = open("input.txt", "r") 
input = file.readlines()
print("PROGRAM STARTED")
left = sorting([line.split()[0] for line in input])
print("LEFT SORTING FINISHED")
right = sorting([line.split()[1] for line in input])
print("RIGHT SORTING FINISHED")


print("SORTED FINISHED, STARTING DIFFERENCE")

with open("left.txt", "w") as file:
    for item in left:
        file.write(f"{item}\n")

with open("right.txt", "w") as file:
    for item in right:
        file.write(f"{item}\n")

# print(f"Len of LEFT: {len(left)}, Len of Right: {len(right)}")

diff = [abs(int(left[i]) - int(right[i])) for i in range(len(left))]

# # # print(f"DIFF:{diff}")
print(sum(diff))
