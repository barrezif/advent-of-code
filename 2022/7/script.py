from collections import deque

sizes = []
class Directory:
    def __init__(self):
        self.subDir = {}
        self.totalSize = 0
        self.totalFromLs = 0

def get_puzzle_input():
    return [line.strip() for line in open('input.txt').readlines()]

def part2():
    pInput = get_puzzle_input()
    r = deque(pInput)
    r.popleft()

    root = makeMap(r, Directory())
    getSize(root)
    
    # For Part 1
    # return sum(sizes)

    i = 0
    unusedSpace = 70000000 - 44359867

    
    sortedSizes = sorted(sizes)
    for i in range(len(sortedSizes)):
        if sortedSizes[i] + unusedSpace >= 30000000:
            return sortedSizes[i]


def makeMap(rows, directory):
    while rows:
        args = rows.popleft().split(" ")
        if args[0] == "$":
            if args[1] == "ls":
                while rows and rows[0].split(" ")[0] != "$":
                    newArgs = rows.popleft().split(" ")
                    if newArgs[0] == "dir":
                        if newArgs[1] not in directory.subDir:
                            directory.subDir[newArgs[1]] = Directory()
                    else:
                        directory.totalFromLs += int(newArgs[0])
            elif args[1] == "cd":
                if args[2] == "..":
                    return directory
                else:
                    makeMap(rows, directory.subDir[args[2]])
    return directory


def getSize(directory:Directory):
    subDirSum = 0
    if directory.subDir:
        for child in directory.subDir.values():
            subDirSum += getSize(child)
    
    directory.totalSize = subDirSum + directory.totalFromLs
    # For Part 1
    # if directory.totalSize <= 100000:
    sizes.append(directory.totalSize)
    return directory.totalSize           

def main():
    print(part2())


if __name__ == '__main__':
    main()


