with open("day3.txt") as puzzle_input:
    ins = puzzle_input.readlines()
    len = len(ins)
    gamma = ""
    epsilon = ""
    power = 0
    count = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
    for line in ins:
        for i, char in enumerate(str(line)[:-1]):
            if char == "1":
                count[i] += 1
    for digit in count.keys():
        if len - count[digit] < len // 2:
            epsilon += "0"
            gamma += "1"
        else:
            epsilon += "1"
            gamma += "0"
    
    print(int(gamma, 2) * int(epsilon, 2))
