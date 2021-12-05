from collections import defaultdict


def get_puzzle_input():
    file = open('day5.txt')
    puzzle_input = [line for line in file.read().split('\n')]
    return puzzle_input

def get_and_save_intermittent_lines(line, points):
    x1, y1 = [int(point) for point in line[0].split(',')]
    x2, y2 = [int(point) for point in line[1].split(',')]

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            points[(x1, i)] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            points[(i, y1)] += 1
    elif abs(x2 - x1) == abs(y2 - y1):
        y1_i = y1
        y2_i = y2
        if x1 < x2:
            for i in range(x1, x2 + 1):
                points[(i, y1)] += 1
                y1 = y1 + 1 if y1_i < y2 else y1 - 1
        else:
            for i in range(x2, x1 + 1):
                points[(i, y2)] += 1
                y2 = y2 + 1 if y2_i < y1 else y2 - 1

def main():
    puzzle_input = get_puzzle_input()
    points = {}
    points = defaultdict(lambda:0, points)
    for line in puzzle_input:
        get_and_save_intermittent_lines([point for point in line.split(' -> ')], points)
    
    return len([val for val in points.values() if val > 1]) 

if __name__ == '__main__':
    print(main())
