puzzle_input = open("day3.txt")
l = puzzle_input.readlines()
m = l[:]

ones = []
zeroes = []
count = 0
while len(l) != 1:
    ones = []
    zeroes = []
    for i in l:
        if i[count] == "1":
            ones.append(i)
        else:
            zeroes.append(i)
    count += 1
    l = ones if len(ones) >= len(zeroes) else zeroes
    
oxygen = l[0]
count = 0
while len(m) > 1:
    ones = []
    zeroes = []
    for i in m:
        if i[count] == "1":
            ones.append(i)
        else:
            zeroes.append(i)
    count += 1
    m = ones if len(ones) < len(zeroes) else zeroes
co2 = m[0]

print(int(oxygen,2) * int(co2,2))
