from collections import Counter, defaultdict, deque

def get_puzzle_input():
    file = open('input.txt')
    puzzle_input = [num.strip() for num in file.readlines()]

    return puzzle_input


def main():
    puzzle_input = get_puzzle_input()
    template = puzzle_input[0]
    pairs = [[item.strip() for item in line.split(' -> ')] for line in puzzle_input[2:]]
    pairs = {pair[0]: pair[1] for pair in pairs}
    counts = Counter(grow(template, 40, pairs))
    
    return counts.most_common()[0][1] - counts.most_common()[-1][1]


def grow(template, steps, pairs):
    letter_count = defaultdict(lambda:0, Counter(template))
    tracker = defaultdict(lambda:0, {template: 1})
    cache = {}

    for _ in range(steps):
        tracker_copy = tracker.copy()
        for s in tracker_copy.keys():
            tracker[s] -= tracker_copy[s]
            if s in cache and tracker_copy[s] != 0:
                for item in cache[s]:
                    letter_count[item[1]] += tracker_copy[s]
                    tracker[item] += tracker_copy[s]
            elif tracker_copy[s] != 0:
                current = []
                for i in range(1, len(s)):
                    substring = s[i - 1: i + 1]
                    if substring in pairs.keys():
                        tracker[s[i - 1:i] + pairs[substring]+ s[i: i + 1]] += tracker_copy[s]
                        letter_count[pairs[substring]] += tracker_copy[s]
                        current.append(s[i - 1:i] + pairs[substring]+ s[i: i + 1])            
                cache[s] = current

    return letter_count


if __name__ == '__main__':
    print(main())