from collections import defaultdict, Counter
from enum import Enum
import math

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

def isSafe(report):
    if report[0] == report[1]:
        return False
    is_descending = int(report[0]) > int(report[1])
    prev = int(report[0])
    for level in report[1:]:
        level = int(level)
        if abs(level-prev) > 3 or abs(level-prev) == 0:
            return False
        if is_descending and level > prev:
            return False
        if not is_descending and level < prev:
            return False
        prev = level
    return True

def part1():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE_SPLIT_BY, " ")
    print(pInput, end="\n\n\n")


    res = 0

    for report in pInput:
        res += isSafe(report)

    return res

def part2():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE_SPLIT_BY, " ")

    res = 0
    for report in pInput:
        is_safe = isSafe(report)
        if is_safe:
            res += 1
        else:
            for i in range(len(report)):
                if isSafe(report[0:i]+report[i+1:]):
                    res += 1
                    break
    return res

def main():
    print("           ", part1())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")

    res_2 = part2()
    if res_2:
        print(res_2)
        print("PART 2 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()

