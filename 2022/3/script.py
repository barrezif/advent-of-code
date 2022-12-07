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
    pInput = get_puzzle_input(InputGroup.LINE)
    print(pInput, end="\n\n\n")
    total = 0
    i = 0
    while i < len(pInput):
        first = set( c for c in pInput[i])
        second = set( c for c in pInput[i+1])
        third = set( c for c in pInput[i+2])

        el = first & second &  third
        ccc = el.pop()
        
        if ccc.islower():
            print(ord(ccc) -96)
            total +=( ord(ccc) - 96)
        else:
            print(ord(ccc) -64, "upper")
            total += (ord(ccc) - 64 + 26)
        
        i += 3

    res = total

    return res


def main():
    print("           ", part1())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()


