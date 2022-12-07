from collections import defaultdict, Counter, deque
from enum import Enum
from typing import List

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

sizes = {}
sizes2 = []
def part1():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.LINE)
    
    
    r = deque(pInput)
    r.popleft()


    root = makeMap(r, Directory(None, "/"))
    getSize(root)

    i = 0
    unusedSpace = 70000000 - 44359867

    sortedSizes = sorted(sizes2)
    for i in range(len(sortedSizes)):
        if sortedSizes[i] + unusedSpace >= 30000000:
            return sortedSizes[i]
        

    
    
    



class Directory:
    def __init__(self, parent, name):
        self.subDir = {}
        self.totalSize = 0
        self.parent = parent
        self.name = name
        self.totalFromLs = 0
    

def makeMap(rows, directory):
    while rows:
        args = rows.popleft().split(" ")
        if args[0] == "$":
            if args[1] == "ls":
                while rows and rows[0].split(" ")[0] != "$":
                    newArgs = rows.popleft().split(" ")
                    # print(4*level*" ", newArgs)
                    if newArgs[0] == "dir":
                        if newArgs[1] not in directory.subDir:
                            directory.subDir[newArgs[1]] = Directory(directory, newArgs[1])
                    else:
                        directory.totalFromLs += int(newArgs[0])
            elif args[1] == "cd":
                if args[2] == "..":
                    return directory
                else:
                    makeMap(rows, directory.subDir[args[2]])
    return directory


def getSize(directory:Directory):
    totalFromChildren = 0
    if directory.subDir:
        for child in directory.subDir.values():
            totalFromChildren += getSize(child)
    directory.totalSize = totalFromChildren + directory.totalFromLs
    sizes2.append(directory.totalSize)
    return directory.totalSize

    # while rows:
    #     args = rows.popleft().split(" ")
    #     if args[0] == "$":
    #         if args[1] == "ls":
    #             while rows and rows[0].split(" ")[0] != "$":
    #                 newArgs = rows.popleft().split(" ")
    #                 # print(4*level*" ", newArgs)
    #                 if newArgs[0] == "dir":
    #                     if newArgs[1] not in directory.subDir:
    #                         raise Exception("This should exist here but doesn't") 
    #         elif args[1] == "cd":
    #             if args[2] == "..":
    #                 directory.totalSize = 0
    #                 for subDir in directory.subDir.values():
    #                     directory.totalSize += subDir.totalSize
    #                 directory.totalSize += directory.totalFromLs
    #                 if directory.totalSize <= 100000:
    #                     sizes[(level, directory.name)] = directory.totalSize
    #                 return
    #             else:
    #                 getSizes(rows, directory.subDir[args[2]], level + 1)
                    

def main():
    print("           ", part1())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")

_end = '_end_'
def make_trie(*words):
     root = dict()
     for word in words:
         current_dict = root
         for letter in word:
             current_dict = current_dict.setdefault(letter, {})
         current_dict[_end] = _end
     return root


if __name__ == '__main__':
    main()


