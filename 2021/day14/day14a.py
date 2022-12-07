from collections import Counter

def get_puzzle_input():
    file = open('input.txt')
    puzzle_input = [num.strip() for num in file.readlines()]

    return puzzle_input


def main():
    template = ""
    pairs = []
    for line in get_puzzle_input():
        if '->' in line:
            pairs.append([item.strip() for item in line.split(' -> ')])
        elif len(line) > 0:
            template = line
    pairs = {pair[0]: pair[1] for pair in pairs}
    print(template, 1, pairs)
    s = grow(template, 40, pairs)
    counts = Counter(s)
    
    print(counts)
    most_common = counts.most_common()[0]
    least_common = counts.most_common()[-1]

    print(most_common[1] - least_common[1])


def grow(template, steps, pairs):
    copy = template
    for _ in range(steps):
        j = 1
        for i, val in enumerate(copy, 1):
            if copy[i - 1: i + 1] in pairs:
                template = template[:j] + pairs[copy[i - 1: i + 1]] + template[j:]
                j += 1
            j += 1
        copy = template
    print(template)
    return template


if __name__ == '__main__':
    main()