def getNum(start, instruction):

    instruct_list = [instruction[0], int(instruction[1:])]

    if instruct_list[0] == "L":
        instruct_list[1] *= -1

    move = start + instruct_list[1]

    if move < 0:
        while move < 0:
            move = 100 + move
    elif move > 99:
        while move > 99:
            move = move - 100

    return move



code_file = open("code.txt", "r")
code = []

for line in code_file:
    line = line.replace("\n", "")
    code.append(line)

current = 50
zeroes = 0
nums = []

for instruction in code:
    num = getNum(current, instruction)
    print(num)
    current = num
    if num == 0:
        zeroes += 1
    nums.append(num)

print("zeroes:" + str(zeroes))
print(len(code))
