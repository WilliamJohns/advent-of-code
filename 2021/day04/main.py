class BingoBoard:
    def __init__(self, lines):
        self.board = {
            (row, col): (int(ch), False)
            for row, line in enumerate(lines)
            for col, ch in enumerate(line.split())
        }
        self.last_mark = None

    def __str__(self):
        print_board = [
            list(range(5))
            for _ in range(5)
        ]
        for (row, col), (val, marked) in self.board.items():
            s = f" {val:2} " if not marked else f"[{val:2}]"
            print_board[row][col] = s

        return "\n".join(
            " ".join(row)
            for row in print_board
        )

    def mark(self, num):
        for coord, (val, _) in self.board.items():
            if val == num:
                self.board[coord] = (val, True)
                self.last_mark = num

    def winner(self):
        row_mark_count = {
            n: 0
            for n in range(5)
        }
        col_mark_count = {
            n: 0
            for n in range(5)
        }
        for (row, col), (_, marked) in self.board.items():
            if marked:
                row_mark_count[row] += 1
                col_mark_count[col] += 1
                if row_mark_count[row] == 5 or col_mark_count[col] == 5:
                    return True
        return False

    def score(self):
        base_score = sum([
            val
            for _, (val, marked) in self.board.items()
            if not marked
        ])
        return base_score*self.last_mark


def part_1(lines) -> None:
    """38913"""
    nums, *board_lines = lines

    line_groups = [
        board_lines[i:i+5]
        for i in range(0, len(board_lines), 5)
    ]
    boards = [
        BingoBoard(group)
        for group in line_groups
    ]

    for num in map(int, nums.split(",")):
        for board in boards:
            board.mark(num)
            if board.winner():
                print(board.score())
                return
    

def part_2(lines) -> None:
    """16836"""
    nums, *board_lines = lines

    line_groups = [
        board_lines[i:i+5]
        for i in range(0, len(board_lines), 5)
    ]
    boards = [
        BingoBoard(group)
        for group in line_groups
    ]

    winning_boards = set()
    board_count = len(boards)
    for num in map(int, nums.split(",")):
        for board_num, board in enumerate(boards):
            if board_num in winning_boards:
                continue

            board.mark(num)
            if board.winner():
                winning_boards.add(board_num)

            if len(winning_boards) == board_count:
                print(board.score())
                return


def main():
    with open("input.txt", "r") as f:
        lines = [
            line.strip()
            for line in f.readlines()
            if line.strip() != ''
        ]

    part_1(lines)
    part_2(lines)


if __name__ == "__main__":
    main()
