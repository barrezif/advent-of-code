def get_puzzle_input_lines():
    """ gets file input and stores into a list by lines"""
    file = open('input.txt')
    puzzle_input = [num.strip() for num in file.readlines()]

    return puzzle_input

def get_adjacent_squares(x, y):
    """ given a point on the 2d array, this returns a list of neighbors """
    row_bound = len(puzzle)
    col_bound = len(puzzle[0])
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    return [(i + x, j + y) for i, j in directions if 0 <= i + x < row_bound and 0 <= j + y < col_bound]


def traverse(i,j, current_basin):
    """ dfs traversal. Skips over squares we've already seen """
    if (i,j) in seen:
        return
    seen.append((i,j))
    if int(puzzle[i][j]) == 9:
        return
    else:
        current_basin.append(int(puzzle[i][j]))
        for x, y in get_adjacent_squares(i,j):
            traverse(x, y, current_basin)
        return current_basin


def main():
    global puzzle, seen
    puzzle = get_puzzle_input_lines()
    
    basins = []
    seen = []
    
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if basin := traverse(i, j, []):
                basins.append(len(basin))
    
    basins = sorted(basins, reverse=True)
    return basins[0] * basins[1] * basins[2]


if __name__ == '__main__':  
    print(main())
