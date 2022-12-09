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

"""
"This is easy! The tail only moves if it's already 1 space behind
the direction the head is moving."
"""
def part1():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE_SPLIT_BY, " ")
    print(pInput, end="\n\n\n")

    currH = [0,0]
    currT = [0,0]
    s = set()
    for direction, distance in pInput:
        for _ in range(int(distance)):
            if direction == "U":
                if currT[1] >= currH[1]:
                    currH[1] += 1
                else:
                    currH[1] += 1
                    currT = [currH[0],currH[1]-1]

            elif direction == "D":
                if currT[1] <= currH[1]:
                    currH[1] -= 1      
                else:
                    currH[1] -= 1
                    currT = [currH[0],currH[1]+1]

            elif direction == "L":
                if currT[0] <= currH[0]:
                    currH[0] -= 1
                else:
                    currH[0] -= 1
                    currT = [currH[0]+1,currH[1]]
                
            elif direction == "R":
                if currT[0] >= currH[0]:
                    currH[0] += 1
                else:
                    currH[0] += 1
                    currT = [currH[0]-1,currH[1]]
    
            s.add((currT[0], currT[1]))
    

    return len(s)

def moveHead(knots, direction):
    if direction == "U":
        knots[0][1] += 1

    elif direction == "D":
        knots[0][1] -= 1 

    elif direction == "L":
        knots[0][0] -= 1

    elif direction == "R":
        knots[0][0] += 1


"""
Took me a while to realize that with the approach for part 1, I was
moving every tail the same way the head moved.

Had to extract the moving head part

THEN, I realized that the direction the head moves doesn't matter
for all of the tails. Head moving up, might mean that one tail moves
left. So the logic from part 1 won't work fully either.

Had to change code so that we're just looking at distance between
two knots to determine whether/where the other moves.

THEN.. I realized that it's possible for an already diagonal tail
to have to move diagonally.
"""
def part2():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE_SPLIT_BY, " ")
    print(pInput, end="\n\n\n")

    knots = [[0,0] for _ in range(10)]
    s = set()
    for direction, distance in pInput:
        for _ in range(int(distance)):
            moveHead(knots, direction)
            for i in range(len(knots)-1):
                if abs(knots[i+1][1] - knots[i][1]) > 1 and abs(knots[i+1][0] - knots[i][0]) > 1:
                    if knots[i+1][1] < knots[i][1]:
                        knots[i+1] = [knots[i+1][0],knots[i][1]-1]
                    else:
                        knots[i+1] = [knots[i+1][0],knots[i][1]+1]
                    
                    if knots[i+1][0] < knots[i][0]:
                        knots[i+1] = [knots[i][0]-1,knots[i+1][1]]
                    else:
                        knots[i+1] = [knots[i][0]+1,knots[i+1][1]]  
                 
                elif abs(knots[i+1][1] - knots[i][1]) > 1:
                    if knots[i+1][1] < knots[i][1]:
                        knots[i+1] = [knots[i][0],knots[i][1]-1]
                    else:
                        knots[i+1] = [knots[i][0],knots[i][1]+1]

                elif abs(knots[i+1][0] - knots[i][0]) > 1:
                    if knots[i+1][0] < knots[i][0]:
                        knots[i+1] = [knots[i][0]-1,knots[i][1]]
                    else:
                        knots[i+1] = [knots[i][0]+1,knots[i][1]]            
            s.add((knots[-1][0], knots[-1][1]))
        print((knots[-1][0], knots[-1][1]))
    return len(s)


def main():
    print("           ", part2())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()


            # print(knots[0])
            # for i in range(len(knots)-1):
            #     print(i)
            #     if direction == "U":
            #         if  knots[i+1][1] >= knots[i][1]:
            #             continue
            #         else:
            #             knots[i+1] = [knots[i][0],knots[i][1]-1]

            #     elif direction == "D":
            #         if knots[i+1][1] <= knots[i][1]:
            #             continue  
            #         else:
            #             knots[i+1] = [knots[i][0],knots[i][1]+1]

            #     elif direction == "L":
            #         if knots[i+1][0] <= knots[i][0]:
            #             continue
            #         else:
            #             knots[i+1] = [ knots[i][0]+1, knots[i][1]]
                    
            #     elif direction == "R":
            #         if knots[i+1][0] >=  knots[i][0]:
            #             continue
            #         else:
            #             knots[i+1] = [knots[i][0]-1, knots[i][1]]