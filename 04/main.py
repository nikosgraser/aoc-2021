from collections import defaultdict
from typing import List, Dict, Tuple, Union


class Board:
    size_h, size_v = 5, 5

    def __init__(self):
        self.fields: Dict[Tuple[int, int], str] = {}
        self.marks: Dict[Tuple[int, int], bool] = defaultdict(lambda: False)
        self.num_rows = 0
        self.won = False

    def add_row(self, row: List[str]):
        for i in range(len(row)):
            self.fields[self.num_rows, i] = row[i]
        self.num_rows += 1

    def _mark(self, number) -> Union[None, Tuple[int, int]]:
        for field, board_num in self.fields.items():
            if board_num == number:
                self.marks[field] = True
                return field
        return None

    def mark_and_check_for_win(self, number: str) -> bool:
        field = self._mark(number)
        if field is None:
            return False
        self.won = all(self.marks[field[0], i] for i in range(Board.size_v)) or all(
            self.marks[j, field[1]] for j in range(Board.size_h)
        )
        return self.won

    def sum_of_unmarked_numbers(self):
        return sum(map(int, [number for field, number in self.fields.items() if not self.marks[field]]))


def read_input():
    with open("04/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def read_and_parse_input():
    lines = read_input()
    numbers = lines[0].split(",")
    boards: List[Board] = []
    for line in lines[1:]:
        if len(line) == 0:
            boards.append(Board())
        else:
            boards[-1].add_row(line.split())
    return numbers, boards


def run():
    run_a()
    run_b()


def run_a():
    numbers, boards = read_and_parse_input()
    for number in numbers:
        for board in boards:
            if board.mark_and_check_for_win(number):
                print(board.sum_of_unmarked_numbers() * int(number))
                exit(0)


def run_b():
    numbers, boards = read_and_parse_input()
    for number in numbers:
        boards_without_win = [b for b in boards if not b.won]
        for board in boards_without_win:
            if board.mark_and_check_for_win(number) and len(boards_without_win) == 1:
                print(board.sum_of_unmarked_numbers() * int(number))
                exit(0)
