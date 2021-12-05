from collections import defaultdict
from typing import DefaultDict


def get_puzzle_input():
    file = open('day5.txt')
    puzzle_input = [line for line in file.read().split('\n')]
    return puzzle_input

def get_and_save_intermittend_lines(line, points):
    print(line)
    point1, point2 = line.split(' -> ')
    x1, y1 = point1.split(',')
    x2, y2 = point2.split(',')

    print(x1, x2, x1 == x2)
    print(y1, y2, y1 == y2)
    if x1 == x2:
        for i in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1): # off by one maybe
            points[(int(x1), i)] += 1
    elif y1 == y2:
        for i in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1): # off by one maybe
            points[(i, int(y1))] += 1



def main():
    puzzle_input = get_puzzle_input()
    horizontal_or_vertical_lines = []
    for line in puzzle_input:
        point1, point2 = line.split(' -> ')
        x1, y1 = point1.split(',') # TODO: same code as line 12-14
        x2, y2 = point2.split(',')

        if x1 == x2 or y1 == y2:
            horizontal_or_vertical_lines.append(line)
    points = {}
    points = defaultdict(lambda:0, points)
    for line in horizontal_or_vertical_lines:
        get_and_save_intermittend_lines(line, points)
    
    count = 0
    for point in points.keys():
        if points[point] > 1:
            count += 1
    return count 

if __name__ == '__main__':
    print(main())
