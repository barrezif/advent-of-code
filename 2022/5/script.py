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
        puzzle_input = [line for line in file.read().split('\n\n')]
    
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
    crates, instructions = get_puzzle_input(InputGroup.BLOCK)
    print(crates, end="\n\n\n")
    stackOfCrates = [[] for _ in range(9)]

    r = 1
    t = []
    for i in range(20):
        t.append(r)
        r = r + 4


    for line in reversed(crates.split("\n")[:-1]):
        for i, val in enumerate(line):
            if i in t and val.isalpha():
                stackOfCrates[(i - 1)//4].append(val)
    
    for line in stackOfCrates:
        print(line)

    for line in instructions.strip().split("\n"):
        instructs = line.strip().split(" ")
        amount = int(instructs[1])
        col = int(instructs[3])-1
        dest = int(instructs[5])-1
        stackOfCrates[dest].extend(stackOfCrates[col][-1 * amount:])
        stackOfCrates[col] = stackOfCrates[col][:-1 * amount]
        print("----------")
        for l in stackOfCrates:
            
            print(l)


    for line in stackOfCrates:
        print(line)


    res = [line[-1] for line in stackOfCrates]


    return "".join(res)


def main():
    print("           ", part1())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()


