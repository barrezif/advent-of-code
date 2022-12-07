
def get_puzzle_input_lines():
    """ gets file input and stores into a list by lines"""
    file = open('input.txt')
    puzzle_input = [num.strip() for num in file.readlines()]

    return puzzle_input



def main():
    puzzle = get_puzzle_input_lines()

    scores = {")": 3, "]": 57, "}": 1197, ">":25137}
    opening = "{([<"
    mapped = {"}":"{", ")":"(", "]":"[",">":"<"}
    
    total = 0
    for line in puzzle:
        cache = []
        for char in line:
            if char in opening:
                cache.append(char)
            else:
                if cache.pop() != mapped[char]:
                    total += scores[char]
                    break
                
    return total


if __name__ == '__main__':  
    print(main())
