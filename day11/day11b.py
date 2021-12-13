def get_puzzle_input():
    """ gets file input and stores into a list by lines"""
    file = open('input.txt')
    puzzle_input = [line.strip() for line in file.readlines()]

    return puzzle_input


def create_dict(puzzle_input):
  c = {}
  for i, row in enumerate(puzzle_input):
    for j, num in enumerate(row):
      c[i,j] = num
  return c

def get_adjacent_squares(x, y):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    return [(x + dx, y + dy) for dx, dy in directions if (x + dx, y + dy) in c]

def other_get_adjacent_squares(x, y, seen):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    return [(x + dx, y + dy) for dx, dy in directions if (x + dx, y + dy) in c and (x + dx, y + dy) not in seen]

def main():
    global c
    p = [[int(char) for char in line] for line in get_puzzle_input()]
    c = create_dict(p)
    for day in range(300):
        flashing_squares = []
        for square in c.keys():
            c[square] += 1
            if c[square] == 10:
                flashing_squares.extend(get_adjacent_squares(square[0], square[1]))
                c[square] = 0
        while flashing_squares:
            current = flashing_squares.pop()
            if c[current] != 0:
                c[current] += 1
                if c[current] == 10:
                    flashing_squares.extend(get_adjacent_squares(current[0], current[1]))
                    c[current] = 0
        if len(set(c.values())) == 1:
            return day + 1

if __name__ == '__main__':
    print(main())

