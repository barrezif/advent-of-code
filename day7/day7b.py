from collections import Counter
def get_puzzle_input():
    file = open('input.txt')
    puzzle_input = [int(num) for num in file.read().split(',')]

    return puzzle_input

def calculate_fuel(distance):
    if distance == 0:
        return 0
    return sum([i for i in range(1, distance + 1)])

def main():
    puzzle_input = get_puzzle_input()
    sorted_test = sorted(puzzle_input)
    guesses = [i for i in range(sorted_test[0], sorted_test[-1])]

    return min([sum([calculate_fuel(abs(num - i)) for i in puzzle_input]) for num in guesses])


if __name__ == '__main__':
    print(main())
