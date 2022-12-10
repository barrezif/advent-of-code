from collections import defaultdict, Counter
from enum import Enum
from bisect import bisect_right
class InputGroup(Enum):
    COMMA = 1
    COMMA_INT = 2
    LINE = 3
    LINE_SPLIT_BY = 4
    LINE_INT = 5
    BLOCK = 6


def get_puzzle_input(groupType, splitter=None):
    file = open('input.txt')

    if groupType == InputGroup.COMMA:
        print("COMMA")
        puzzle_input = [line for line in file.read().split(',')]

    elif groupType == InputGroup.COMMA:
        print("COMMA_INT")
        puzzle_input = [int(line) for line in file.read().split(',')]
    
    elif groupType == InputGroup.BLOCK:
        print("BLOCK")
        puzzle_input = [line.strip() for line in file.read().split('\n\n')]
    
    elif groupType == InputGroup.LINE:
        print("LINE")
        puzzle_input = [line.strip() for line in file.readlines()]

    elif groupType == InputGroup.LINE_INT:
        print("LINE_INT")
        puzzle_input = [int(line) for line in file.readlines()]
    
    else:
        print("LINE_SPLIT_BY")
        puzzle_input = [line.strip().split(splitter) for line in file.readlines()]

    return puzzle_input

def part1():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE_SPLIT_BY, " ")
    print(pInput, end="\n\n\n")
    signalsOfInterest = [18,58,98,138,178,218]

    cycleVal = {}
    currCycle = 1
    currVal = 1
    for row in pInput:
        if row[0] == "noop":
            currCycle += 1
        else:
            
            if row[1][0] == "-":
                currVal -= int(row[1][1:])
                cycleVal[currCycle] = currVal
            else:
                currVal += int(row[1])
                cycleVal[currCycle] = currVal
            currCycle += 2
    
    print(cycleVal)

    res = 0
    sl = sorted(cycleVal.keys())
    for s in signalsOfInterest:

        print(bisect_right(sl, s), sl[bisect_right(sl, s)-1], cycleVal[sl[bisect_right(sl, s)-1]])
        res += (cycleVal[sl[bisect_right(sl, s)-1]] * (s+2))

        # res.append(cycleVal[bisect_left(list(cycleVal.keys()), s)])
    

    return res


def part2():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE_SPLIT_BY, " ")
    signalsOfInterest = [i for i in range(-1,239)]
    cycleVal = {0:1}
    currCycle = 1
    currVal = 1
    for row in pInput:
        if row[0] == "noop":
            currCycle += 1
        else:
            currCycle += 2
            if row[1][0] == "-":
                currVal -= int(row[1][1:])
                cycleVal[currCycle] = currVal
            else:
                currVal += int(row[1])
                cycleVal[currCycle] = currVal
            
    sl = sorted(cycleVal.keys())

    
    crt = ["" for _ in range(6)]
    for i, val in enumerate(signalsOfInterest):
        row = i // 40

        print(i+1, val, bisect_right(sl, val), sl[bisect_right(sl, val) -1], cycleVal[sl[bisect_right(sl, val)-1]], val%40)
        if cycleVal[sl[bisect_right(sl, i+1)-1]] in [(i+1)%40, i%40, (i-1)%40]:
            crt[row] += "#"
        else:
            crt[row] += " "

    for row in crt:
        print(row)





def main():
    print("           ", part2())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()


