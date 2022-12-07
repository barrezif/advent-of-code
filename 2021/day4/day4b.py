class Board:
    def __init__(self, board: list[list]):
        self.board = board
        self.positions = {self.board[j][i]: (i, j, False) for i in range(len(self.board)) for j in range(len(self.board))}
        self.row_count = [[] for _ in range(5)]
        self.col_count = [[] for _ in range(5)]
    
    def check_row(self, row: int) -> bool:
        if len(self.row_count[row]) == 5:
            return True
        return False

    def check_column(self, col: int) -> bool:
        if len(self.col_count[col]) == 5:
            return True
        return False
    
    def calculate_board_score(self):
        return sum(int(i) for i in self.positions.keys() if not self.positions[i][2])

    def mark(self, num):
        row = self.positions[num][0]
        col = self.positions[num][1]
        self.row_count[row].append(1)
        self.col_count[col].append(1)
        self.positions[num] = (self.positions[num][0], self.positions[num][1], True)
        return self.check_column(col) or self.check_row(row)



def get_puzzle_input():
    file = open('day4.txt')
    puzzle_input = [line for line in file.read().split('\n\n')]
    return puzzle_input


def mark_and_check_boards(boards, num, winning_boards):
    winners = []
    for board in boards:
        if board not in winning_boards and num in board.positions:
            if board.mark(num):
                winners.append(board)
    return winners

def transform_input_to_bingo():
    puzzle_input = get_puzzle_input()
    draw_order = puzzle_input[0]
    boards = [Board([b.split() for b in board.split('\n')]) for board in puzzle_input[1:]]
    return (draw_order, boards)

def main():
    draw_order, boards = transform_input_to_bingo()
    winning_boards = []
    last_score = 0
    for num in draw_order.split(','):
        winning_boardss = mark_and_check_boards(boards, num, winning_boards)
        if winning_boardss:
            for final_board in winning_boardss:
                winning_boards.append(final_board)
                last_score = int(num) * int(final_board.calculate_board_score())
    return last_score

if __name__ == '__main__':
    print(main())
