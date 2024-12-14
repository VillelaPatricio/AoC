digits = [str(x) for x in range(10)]
mul_count = 0
final_count = 0
can_add = True

def check_3digits(string, index):
    number = ""
    for i in range(3):
        if string[i+index] in digits:
            number += string[i+index]
        else:
            return int(number)
    return int(number)

with open("data.txt", "r") as file:
    for line in file:
        for i, char in enumerate(line):
            if (line[i:i+4]) == str("do()"):
                can_add = True
            elif (line[i:i+7]) == str("don't()"):
                can_add = False
            elif ((line[i:i+4]) == str("mul(")) and (line[i+4] in digits):
                substring = line[i:i+12]
                first_num = check_3digits(substring, 4)
                if substring[4+len(str(first_num))] == ",":
                    second_num = check_3digits(substring,(5+len(str(first_num))))
                    print(substring)
                    print(first_num)
                    print(second_num)
                    if substring[5+len(str(first_num))+len(str(second_num))] == ")" and can_add == True:
                        final_count += (first_num * second_num)


print(final_count)