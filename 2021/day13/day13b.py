from collections import Counter, defaultdict
from itertools import zip_longest

def get_puzzle_input():
    file = open('input.txt')
    puzzle_input = [num.strip() for num in file.read().split("\n\n")]

    return puzzle_input


def get_dimensions(puzzle_input):
    width = 0
    height = 0
    dot_coords = []
    for line in puzzle_input.split('\n'):
        x, y = [int(num) for num in line.split(",")]
        if x > width:
            width = x
        if y > height:
            height = y
        dot_coords.append((x, y))
            
    return width, height, dot_coords


def setup_sheet(width, height, dot_coords):
    sheet = []
    for x in range(height+1):
        sheet_row = []
        for y in range(width+1):
            if (y,x) in dot_coords:
                sheet_row.append("@")
            else:
                sheet_row.append(" ")
        sheet.append(sheet_row)
    return sheet


def fold(sheet, fold_point, y_axis):
    half_one = []
    if y_axis:
        half_one = sheet[:fold_point]
        half_two = sheet[fold_point + 1:]

        for i, row in enumerate(half_two):
            for j, val in enumerate(row):
                if val == '@':
                    half_one[fold_point - 1 - i][j] = '@'
    else:
        half_one = []
        half_two = []
        for i, row in enumerate(sheet):
            half_one.append(row[:fold_point])
            half_two.append(row[fold_point + 1:])

        for i, row in enumerate(half_two):
            for j, val in enumerate(row):
                if val == '@':
                    half_one[i][fold_point - 1 - j] = '@'

    return half_one


def get_folds(fold_input):
    folds = []
    for row in fold_input.split('\n'):
        row = row.replace('fold along ', '')
        x, val = row.strip().split('=')
        folds.append((x.strip()=='y', int(val)))
    
    return folds


def main():
    nums, fold_input = [item.strip() for item in get_puzzle_input()]
    width, height, coords = get_dimensions(nums)
    folds = get_folds(fold_input)
    sheet = setup_sheet(width, height, coords)
    
    for f in folds:
        sheet = fold(sheet, f[1], f[0])

    for row in sheet:
        print(row)
    
if __name__ == '__main__':
    main()
