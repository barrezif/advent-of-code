with open("day1.txt") as fp:
    prev = None
    count = 0
    for line in fp:
        if prev != None and int(line) > prev:
            count += 1
        prev = int(line)
    print(count)