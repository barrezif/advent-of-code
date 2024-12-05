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

KEY="XMAS"

def is_oob(x,y,row_bound):
    if x < 0 or y < 0:
        return True
    if x >= row_bound or y >= row_bound:
        return True
    return False

def find_word(x, y, word_indx, word_map, direction):
    if is_oob(x, y, len(word_map[0])):
        return False
    print(word_map[x][y], KEY[word_indx])
    if word_map[x][y] != KEY[word_indx]:
        # print("No Match")
        return False
    if KEY[word_indx] == "S":
        print("FOUND A MATCH")
        return True
    print("recursing")
    return find_word(x+direction[0], y+direction[1], word_indx+1, word_map, direction)


def part1():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE)
    # print(pInput, end="\n\n\n")

    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    res = 0
    for i, row in enumerate(pInput):
        for j, val in enumerate(row):
            if val == "X":
                for direction in directions:
                    if find_word(i+direction[0],j+direction[1],1,pInput,direction):
                        print("Found word at ", i, j, "with direction ", direction)
                        res += 1
    return res

def is_mas(x, y, word_map, directions):
    if any(is_oob(x+d[0], y+d[1], len(word_map[0])) for d in directions):
        return False
    letters = set(word_map[x][y])
    for direction in directions:
        letters.add(word_map[x+direction[0]][y+direction[1]])
    return letters == set("MAS")

def part2():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE)
    # print(pInput, end="\n\n\n")

    directions = [[(-1,-1), (1,1)],[(-1,1), (1,-1)]]

    res = 0
    for i, row in enumerate(pInput):
        for j, val in enumerate(row):
            if val == "A":
                if all([is_mas(i,j,pInput,direction) for direction in directions]):
                    print("Found x-mas at ", i, j)
                    res += 1
    return res

def main():
    # print("           ", part1())
    # print("PART 1 ^^^^^^^^^^^^^^^^^^")

    res_2 = part2()
    if res_2:
        print(res_2)
        print("PART 2 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()


