from collections import defaultdict, Counter, deque
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

class Monkey:
    monkeyCount = -1
    operatorMap = {
        "+":lambda x,y:x+y,
        "*": lambda x,y:x*y
    }
    monkeyList = {}
    itemCache = {}

    def __init__(self, inputBlock):
        Monkey.monkeyCount += 1
        self.mId = Monkey.monkeyCount
        self.items = deque([])
        self.operation = ""
        self.divider = 1
        self.trueMonkey = None
        self.falseMonkey = None
        self.inspectedCount = 0
        self.setUp(inputBlock)


    def setUp(self, inputBlock):
        characteristics = [c.strip() for c in inputBlock.split("\n")]

        _, startingItems = characteristics[1].split(": ")
        _, operation = characteristics[2].split("=")
        self.items = deque([int(s) for s in startingItems.split(",")])
        self.operation = operation.strip()
        self.divider = int(characteristics[3].strip().split("divisible by")[1])
        self.trueMonkey = int(characteristics[4].strip().split("monkey")[1])
        self.falseMonkey = int(characteristics[5].strip().split("monkey")[1])
        Monkey.monkeyList[self.mId] = self
    
    def takeTurn(self):
        _, operator, num = self.operation.strip().split(" ")
        old_num = num

        while self.items:
            
            self.inspectedCount += 1
            item = self.items.popleft()
            # print(item)
            if old_num == "old":
                num = item
            else:
                num = int(old_num)

            divisors = [i for i in range(1,int(math.sqrt(num))) if num % i == 0]
            divisors = tuple(divisors)

            for cachedItem in Monkey.itemCache:
                print(len(set(divisors) - set(cachedItem)))
                if len(set(divisors) - set(cachedItem)) == 0:
                    print("HERERERE")
                num = Monkey.itemCache[divisors]
                Monkey.monkeyList[self.trueMonkey].items.append(num)
                print("\n\n\n HERE")
                return 
            
            
            # print(item, operator, num, Monkey.operatorMap[operator](item, num))
            
            # investigate
            scoreAfterInvestigating = Monkey.operatorMap[operator](item, num)
            remainder = scoreAfterInvestigating % 3
            scoreAfterInvestigating = scoreAfterInvestigating // 3
            Monkey.itemCache[divisors] = scoreAfterInvestigating

            
            if scoreAfterInvestigating % self.divider == 0:
                print(scoreAfterInvestigating, "Divisible by ", self.divider)
                print("Throw to Monkey ", self.trueMonkey)
                Monkey.monkeyList[self.trueMonkey].items.append(scoreAfterInvestigating)
            else:
                # print("Not Divisible by ", self.divider)
                # print("Throw to Monkey ", self.falseMonkey)
                Monkey.monkeyList[self.falseMonkey].items.append(scoreAfterInvestigating)


    def __repr__(self):
        return f'{self.mId=}: {self.items=}, {self.operation=}, {self.divider=}, {self.trueMonkey=}, {self.falseMonkey=}'
        
def part1():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    monkeyList = get_puzzle_input(InputGroup.BLOCK)
    print(monkeyList, end="\n\n\n\n\n\n\n")

    monkeys = []
    for monkey in monkeyList:
        monkeys.append(Monkey(monkey))
    
    # cache = set()
    # repeatList = defaultdict(list)
    for i in range(20):
        # repeated = False
        for monkey in monkeys:
            # print(monkey)
            monkey.takeTurn()
        #     # print(stats)
        #     if stats in cache:
        #         # print("IT REPEATS!!!!!!", i)
        #         repeatList[monkey.mId].append(i)
        #     cache.add(stats)
        # if repeated:
        #     break
        # print("+"*30)
    # for k,v in repeatList.items():
    #     print(k,v)
    
    inspectedCounts = []

    for monkey in monkeys:
        inspectedCounts.append(monkey.inspectedCount)
        # print(monkey)

    inspectedCounts = sorted(inspectedCounts)
    res = inspectedCounts[-1]* inspectedCounts[-2]

    return res


def main():
    print("           ", part1())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()


