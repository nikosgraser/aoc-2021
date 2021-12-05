from collections import defaultdict
from typing import Dict, Tuple, List

Coordinate = Tuple[int, int]


class Grid:
    def __init__(self):
        self._grid: Dict[Coordinate, int] = defaultdict(int)

    def add_line(self, start: Coordinate, end: Coordinate, allow_diagonal=False):
        if start[0] != end[0] and start[1] != end[1] and not allow_diagonal:
            return
        step0, step1 = cmp(start[0], end[0]), cmp(start[1], end[1])
        current = start
        while current != end:
            self._grid[current] += 1
            current = (current[0] + step0, current[1] + step1)
        self._grid[end] += 1

    def num_coordinates_with_overlapping_lines(self) -> int:
        return sum(1 for k, v in self._grid.items() if v > 1)


def cmp(a: int, b: int) -> int:
    return 0 if a == b else (b - a) // (abs(b - a))


def read_input():
    with open("05/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def parse_coordinate(s: str) -> Coordinate:
    return tuple(map(int, s.split(",")))


def parse_line(line: str) -> Tuple[Coordinate, Coordinate]:
    start_and_end = line.split(" -> ")
    return parse_coordinate(start_and_end[0]), parse_coordinate(start_and_end[1])


def parse_input(allow_diagonal: bool) -> Grid:
    grid = Grid()
    lines = read_input()
    for line in lines:
        start, end = parse_line(line)
        grid.add_line(start, end, allow_diagonal)
    return grid


def run():
    run_a()
    run_b()


def run_a():
    grid = parse_input(False)
    print(grid.num_coordinates_with_overlapping_lines())


def run_b():
    grid = parse_input(True)
    print(grid.num_coordinates_with_overlapping_lines())
