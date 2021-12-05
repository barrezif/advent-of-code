from collections import defaultdict

def get_puzzle_input():
    file = open('day5.txt')
    puzzle_input = [line for line in file.read().split('\n')]
    return puzzle_input

def get_and_save_intermittend_lines(line, points):
    x1, y1 = [int(point) for point in line[0].split(',')]
    x2, y2 = [int(point) for point in line[1].split(',')]
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            points[(x1, i)] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            points[(i, y1)] += 1

def main():
    puzzle_input = get_puzzle_input()
    horizontal_or_vertical_lines = []
    points = defaultdict(lambda:0, {})

    for line in puzzle_input:
        point1, point2 = line.split(' -> ')
        x1, y1 = point1.split(',')
        x2, y2 = point2.split(',')
        if x1 == x2 or y1 == y2:
            horizontal_or_vertical_lines.append([point for point in line.split(' -> ')])
    
    for line in horizontal_or_vertical_lines:
        get_and_save_intermittend_lines(line, points)
    
    return len([val for val in points.values() if val > 1]) 

if __name__ == '__main__':
    print(main())
