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
    rows = get_puzzle_input(InputGroup.LINE)
    print(rows, end="\n\n\n")

    forest = [[int(t) for t in row] for row in rows]
    print(forest)

    total_vis = set()
    for i, row in enumerate(forest):
        next_vis = -1
        for j, val in enumerate(row):
            if val > next_vis:
                total_vis.add((i,j))
                next_vis = val
    print(len(total_vis))
    
    

    for i in range(len(forest)-1, -1, -1):
        next_vis = -1
        for j in range(len(forest[i])-1, -1,-1):
            print(i,j, forest[i][j])
            if forest[i][j] > next_vis:
                total_vis.add((i,j))
                next_vis = forest[i][j]
    print(len(total_vis))
    

    for i, _ in enumerate(forest[0]):
        next_vis = -1
        for j, row in enumerate(forest):
            if row[i] > next_vis:
                total_vis.add((j,i))
                next_vis = row[i]
    print(len(total_vis))
    
    for i in range(len(forest[0])-1, -1, -1):
        next_vis = -1
        for j in range(len(forest)-1, -1,-1):
            if forest[j][i] > next_vis:
                total_vis.add((j,i))
                next_vis = forest[j][i]


    return len(total_vis)



def part2():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    rows = get_puzzle_input(InputGroup.LINE)
    for row in rows:
        print(row)

    forest = [[int(t) for t in row] for row in rows]
    scores = [[1 if r != 0 and r != len(row)-1 and i != 0 and i != len(rows) -1 else 0 for r in range(len(row))] for i, row in enumerate(rows)]
    

    # reminds me of https://leetcode.com/problems/spiral-matrix/
    # spent so much time debugging this..............
    for i, row in enumerate(forest):
        for j, val in enumerate(row):
            ii = j - 1
            while ii >= 0 and val > row[ii]:
                ii -= 1
            if ii < 0:
                ii = 0
            scores[i][j] *= (j-ii)

    for i in range(len(forest)-1, -1, -1):
        for j in range(len(forest[i])-1, -1,-1):
            ii = j + 1
            while ii < len(forest[i]) and forest[i][j] > forest[i][ii]:
                ii += 1
            if ii > len(forest[i]) - 1:
                ii = len(forest[i]) - 1
            scores[i][j] *= ii-j
    

    for i, _ in enumerate(forest[0]):
        for j, row in enumerate(forest):
            ii = j - 1
            while ii >= 0 and row[i] > forest[ii][i]:
                ii -= 1
            if ii < 0:
                ii = 0
            scores[j][i] *= j-ii
    
    for i in range(len(forest[0])-1, -1, -1):
        for j in range(len(forest)-1, -1,-1):
            ii = j + 1
            while ii < len(forest) and forest[j][i] > forest[ii][i]:
                ii += 1
            if ii > len(forest) -1:
                ii = len(forest) - 1
            print((j,i), (forest[j][i], forest[ii][i]), ii-j)
            scores[j][i] *= ii - j 
    
    max_score = 0
    for s in scores:
        max_score = max(max_score, max(s))

    return max_score
    

def main():
    print("           ", part1())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")
    print(part2())

if __name__ == '__main__':
    main()


