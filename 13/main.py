from collections import defaultdict
from typing import List, Tuple, Dict, Set

Coordinate = Tuple[int, int]


class Fold:
    def __init__(self, axis: str, value: int):
        self.axis = axis
        self.value = value


class Grid:
    def __init__(self):
        self._grid: Dict[Coordinate, bool] = defaultdict(bool)

    def __str__(self):
        min_x = min(coordinate[0] for coordinate, is_point in self._grid.items() if is_point)
        max_x = max(coordinate[0] for coordinate, is_point in self._grid.items() if is_point)
        min_y = min(coordinate[1] for coordinate, is_point in self._grid.items() if is_point)
        max_y = max(coordinate[1] for coordinate, is_point in self._grid.items() if is_point)
        representation = ""
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                representation += "#" if self._grid[(x, y)] else " "
            representation += "\n"
        return representation

    def add_point(self, point: Coordinate):
        self._grid[point] = True

    def _points_below(self, y: int) -> Set[Coordinate]:
        return {coordinate for coordinate, is_point in self._grid.items() if is_point and coordinate[1] > y}

    def _points_rightof(self, x: int) -> Set[Coordinate]:
        return {coordinate for coordinate, is_point in self._grid.items() if is_point and coordinate[0] > x}

    def _realign(self):
        min_x = min(coordinate[0] for coordinate in self._grid.keys())
        min_y = min(coordinate[1] for coordinate in self._grid.keys())
        new_grid: Dict[Coordinate, bool] = defaultdict(bool)
        for coordinate, is_point in self._grid.items():
            new_grid[(coordinate[0] - min_x, coordinate[1] - min_y)] = is_point
        self._grid = new_grid

    def fold(self, fold: Fold):
        if fold.axis == "x":
            self.left_fold(fold.value)
        else:
            self.up_fold(fold.value)
        self._realign()

    def up_fold(self, row: int):
        for coordinate in self._points_below(row):
            new_y = 2 * row - coordinate[1]
            self._grid[(coordinate[0], new_y)] = True
            self._grid[coordinate] = False

    def left_fold(self, col: int):
        for coordinate in self._points_rightof(col):
            new_x = 2 * col - coordinate[0]
            self._grid[(new_x, coordinate[1])] = True
            self._grid[coordinate] = False

    def num_dots(self) -> int:
        return sum(1 for coordinate, is_point in self._grid.items() if is_point)


def read_input():
    with open("13/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def run():
    run_a()
    run_b()


def parse_input() -> Tuple[Grid, List[Fold]]:
    grid = Grid()
    folds: List[Fold] = []
    lines = read_input()
    for line in lines:
        if "," in line:
            point_raw = [int(s) for s in line.split(",")]
            grid.add_point((point_raw[0], point_raw[1]))
        elif line.startswith("fold"):
            fold_raw = line[11:].split("=")
            folds.append(Fold(fold_raw[0], int(fold_raw[1])))
    return grid, folds


def run_a():
    grid, folds = parse_input()
    grid.fold(folds[0])
    print(grid.num_dots())


def run_b():
    grid, folds = parse_input()
    for fold in folds:
        grid.fold(fold)
    print(grid)
