from heapq import heapify, heappop, heappush


def get_puzzle_input():
    file = open('input.txt')
    return [line.strip() for line in file.readlines()]


def solve():
    pInput = [[ll for ll in l] for l in get_puzzle_input()]

    LENX = len(pInput[0])
    LENY = len(pInput)

    directions = [[-1,0], [1,0], [0, -1], [0,1]]

    def findEnd():
        for i in range(len(pInput)):
            for j in range(len(pInput[i])):
                if pInput[i][j] == "E":
                    pInput[i][j] = "z"
                    return [i,j]


    def findStart():
        for i in range(len(pInput)):
            for j in range(len(pInput[i])):
                if pInput[i][j] == "S":
                    pInput[i][j] = "a"
                    heap.append((0,i,j))
                    return

    def findStart2():
        for i in range(len(pInput)):
            for j in range(len(pInput[i])):
                if pInput[i][j] == "S":
                    pInput[i][j] = "a"
                if pInput[i][j] == "a":
                    heap.append((0,i,j))


    heap = []
    findStart() # or findStart2()
    heapify(heap)
    
    DESTINATION = findEnd()
    
    visited = set()

    while heap:
        level, row, col = heappop(heap)
        if (row , col) == (DESTINATION[0], DESTINATION[1]):
            return level
        if (row, col) in visited:
            continue
        visited.add((row, col))

        for drow, dcol in directions:
            if col + dcol >= 0 and row + drow >= 0 and col + dcol < LENX and row + drow < LENY:
                if (ord(pInput[row + drow][col + dcol]) - ord(pInput[row][col]) <= 1):
                    heappush(heap, (level + 1, row + drow, col + dcol))



def main():
   print(solve())

if __name__ == '__main__':
    main()


