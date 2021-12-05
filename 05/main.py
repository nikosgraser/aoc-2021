from collections import defaultdict
from typing import Dict, Tuple, List

Coordinate = Tuple[int, int]


class Grid:
    def __init__(self):
        self._grid: Dict[Coordinate, int] = defaultdict(int)

    def add_line_hv(self, start: Coordinate, end: Coordinate, axis: int):
        for step in range(start[axis], end[axis] + 1):
            step_coordinate = [-1, -1]
            step_coordinate[axis] = step
            step_coordinate[(axis + 1) % 2] = start[(axis + 1) % 2]
            self._grid[tuple(step_coordinate)] += 1

    def add_line(self, start: Coordinate, end: Coordinate):
        if start[0] == end[0]:
            axis = 1
        elif start[1] == end[1]:
            axis = 0
        else:
            return
        if start[axis] > end[axis]:
            start, end = end, start
        self.add_line_hv(start, end, axis)

    def num_coordinates_with_overlapping_lines(self) -> int:
        return sum(1 for k, v in self._grid.items() if v > 1)


def read_input():
    with open("05/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def parse_coordinate(s: str) -> Coordinate:
    return tuple(map(int, s.split(",")))


def parse_line(line: str) -> Tuple[Coordinate, Coordinate]:
    start_and_end = line.split(" -> ")
    return parse_coordinate(start_and_end[0]), parse_coordinate(start_and_end[1])


def run():
    run_a()
    run_b()


def run_a():
    grid = Grid()
    lines = read_input()
    for line in lines:
        start, end = parse_line(line)
        grid.add_line(start, end)
    print(grid.num_coordinates_with_overlapping_lines())


def run_b():
    # Implementation starts here
    raise NotImplementedError()
