from collections import defaultdict, Counter
from enum import Enum

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

    d = {"X":1, "Y":2, "Z":3, "A":1,"B":2, "C":3}
    
    him_score = 0
    me_score = 0

    for him, me in pInput:
        if him == "A":
            if me == "X":
                
                me_score += 3
            if me == "Y":
                me_score += 4
                
            if me == "Z":
                me_score += 8
                
        elif him == "B":
            if me == "X":
                
                me_score += 1
            if me == "Y":
                me_score += 5
                
            if me == "Z":
                me_score += 9
                
        elif him == "C":
            if me == "X":
                him_score += 3
                me_score += 2
            if me == "Y":
                me_score += 6
                him_score += 9
            if me == "Z":
                me_score += 7
                him_score += 6

    

    return me_score

def part2():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE_SPLIT_BY)
    print(pInput, end="\n\n\n")


    res = []

    return res

def main():
    print("           ", part1())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")
    # print("           ", part2())
    # print("PART 2 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()


