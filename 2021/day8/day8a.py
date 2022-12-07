from collections import Counter
def get_puzzle_input():
    file = open('input.txt')
    puzzle_input = [num for num in file.readlines()]

    return puzzle_input


pi = get_puzzle_input()

count = 0
for numbers in pi:
    numbers = numbers.split(" | ")
    nums = numbers[1].split(" ")
    for num in nums:
        if len(num.strip()) in [7, 3, 4, 2]:
            count += 1

print(count)


