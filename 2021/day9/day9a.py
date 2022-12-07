
def get_puzzle_input_lines():
    """ gets file input and stores into a list by lines"""
    file = open('input.txt')
    puzzle_input = [num.strip() for num in file.readlines()]

    return puzzle_input


def main():
    puzzle_input = get_puzzle_input_lines()
    sum_of_risks = 0

    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):

            adjacents = []
            if i - 1 >= 0:
                adjacents.append(int(puzzle_input[i-1][j]) + 1)
            if i + 1 < len(puzzle_input):
                adjacents.append(int(puzzle_input[i+1][j]) + 1)
            if j - 1 >= 0:
                adjacents.append(int(puzzle_input[i][j-1]) + 1)
            if j + 1 < len(puzzle_input[i]):
                adjacents.append(int(puzzle_input[i][j+1]) + 1)

            if int(puzzle_input[i][j]) + 1 < min(adjacents):
                sum_of_risks += int(puzzle_input[i][j]) + 1
    
    return sum_of_risks


if __name__ == '__main__':  
    print(main())
