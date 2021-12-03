with open("day2.txt") as puzzle_input:
    x = y = 0
    for line in puzzle_input:
        match line.split(" "):
            case ["forward", steps]:
                x += int(steps)
            case ["up", steps]:
                y -= int(steps)
            case ["down", steps]:
                y += int(steps)
    
    print(x * y)