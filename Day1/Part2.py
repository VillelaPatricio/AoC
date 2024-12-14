with open("left.txt", "r") as file:
    left = [int(line.strip()) for line in file]

with open("right.txt", "r") as file:
    right = [int(line.strip()) for line in file]

repeated = []
finished = False
rep_i = 0
left_i = 0
right_i = 0

while right_i < len(left):
    if left[left_i] == right[right_i]:
        rep_i += 1
        right_i += 1
    elif rep_i != 0:
        repeated.append(rep_i*left[left_i])
        rep_i = 0
    elif left[left_i] < right[right_i]:
        left_i += 1
    elif left[left_i] > right[right_i]:
        right_i += 1


print(repeated)        
print(sum(repeated))