with open("day2.txt") as puzzle_input:
    x = y = aim = 0
    for line in puzzle_input:
        match line.split():
            case ["forward", steps]:
                x += int(steps)
                y += aim * int(steps)
            case ["up", steps]:
                aim -= int(steps)
            case ["down", steps]:
                aim += int(steps)
    
    print(x * y)