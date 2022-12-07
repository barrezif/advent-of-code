from collections import Counter
def get_puzzle_input():
    file = open('input.txt')
    puzzle_input = [int(num) for num in file.read().split(',')]

    return puzzle_input

def main():
    puzzle_input = get_puzzle_input()
    sorted_test = sorted(puzzle_input)
    mean = sum(puzzle_input)//len(puzzle_input)
    median = sorted_test[len(sorted_test)//2]
    counts = Counter(puzzle_input)
    mode = counts.most_common()[0][0]
    guesses = [mean, median, mode]


    return min([sum([abs(num - i) for i in puzzle_input]) for num in guesses])

if __name__ == '__main__':
    print(main())
