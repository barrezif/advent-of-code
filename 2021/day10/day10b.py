# TODO: clean up code
from collections import defaultdict, deque

def get_puzzle_input_lines():
    """ gets file input and stores into a list by lines"""
    file = open('input.txt')
    puzzle_input = [num.strip() for num in file.readlines()]

    return puzzle_input



def main():
    puzzle = get_puzzle_input_lines()

    syntax = {")": 1, "]": 2, "}":3, ">":4}
    opening = "{([<"
    closing = "})]>"
    mapped1 = {"}":"{", ")":"(", "]":"[",">":"<"}
    mapped2 = {"{":"}", "(":")", "[":"]","<":">"}
    
    res = []
    for line in puzzle:
        cache = deque()
        good = True
        for char in line:
            if char in opening:
                cache.append(char)
            else:
                if cache.pop() != mapped1[char]:
                    good = False
                    break
        if good:
            print(cache)
            closing = []
            while cache:
                closing.append(mapped2[cache.pop()])
            score = 0
            for i in closing:
                score = (score * 5) + int(syntax[i])
            res.append(score)
    res = sorted(res)
    
        
                
    return res[len(res)//2]


if __name__ == '__main__':  
    print(main())
