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

class Page:
    def __init__(self, rule_number):
        self.id = rule_number
        self.prev = set()
        self.children = set()

    def __repr__(self) -> str:
        return str(self.id)

def fix_order(pages_in_row, page_map):
    start = None
    for page in pages_in_row:
        if not page_map[page].prev or not any([True if p.id in pages_in_row else False for p in page_map[page].prev]):
            start = page_map[page]
            break    
    pages_in_row.remove(start.id)
    res = [start.id]
    in_row = pages_in_row.copy()
    while pages_in_row:
        curr = start
        for child in curr.children:
            if child.id in pages_in_row and all(True if p.id not in in_row or p.id in res else False for p in page_map[child.id].prev):
                res.append(child.id)
                pages_in_row.remove(child.id)
                curr = child
    print(res)
    return res

def part1():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.BLOCK)
    res = 0

    print(pInput, end="\n\n\n")

    order_rules, pages_to_update = pInput
    pages:dict[int, Page] = {}


    # initialize the page map
    for row in order_rules.split("\n"):
        left, right = [int(digit) for digit in row.split("|")]
        if left not in pages:
            pages[left] = Page(left)
        if right not in pages:
            pages[right] = Page(right)
        pages[left].children.add(pages[right])
        pages[right].prev.add(pages[left])

    # check that the orders are right
    for update in pages_to_update.split("\n"):
        split_update = update.split(',')
        seen = set()
        in_row = set()
        for page in split_update:
            in_row.add(int(page))
        valid = True
        for i, page in enumerate(split_update):
            if not all(True if p.id not in in_row or p.id in seen else False for p in pages[int(page)].prev):
                valid = False
                break
            seen.add(int(page))
        if valid:
            middle_indx = len(split_update)//2
            res += int(split_update[middle_indx])

    return res

def part2():
        # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.BLOCK)
    res = 0

    print(pInput, end="\n\n\n")

    order_rules, pages_to_update = pInput
    pages:dict[int, Page] = {}


    # initialize the page map
    for row in order_rules.split("\n"):
        left, right = [int(digit) for digit in row.split("|")]
        if left not in pages:
            pages[left] = Page(left)
        if right not in pages:
            pages[right] = Page(right)
        pages[left].children.add(pages[right])
        pages[right].prev.add(pages[left])

    # check that the orders are right
    for update in pages_to_update.split("\n"):
        split_update = update.split(',')
        seen = set()
        in_row = set()
        for page in split_update:
            in_row.add(int(page))
        valid = True
        for i, page in enumerate(split_update):
            if not all(True if p.id not in in_row or p.id in seen else False for p in pages[int(page)].prev):
                valid = False
                break
            seen.add(int(page))
        if not valid:
            fixed = fix_order(in_row, pages)
            middle_indx = len(fixed)//2
            print("adding to the res, ", res, int(fixed[middle_indx]))
            res += int(fixed[middle_indx])

    return res

def main():
    print("           ", part2())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")

    # res_2 = part2()
    # if res_2:
    #     print(res_2)
    #     print("PART 2 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()


