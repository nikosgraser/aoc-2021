from collections import defaultdict
from typing import Dict, Tuple, Union, List

Coordinate = Tuple[int, int]


class Octopus:
    MAX_ENERGY = 9

    def __init__(self, starting_energy: int):
        self.energy = starting_energy
        self.flashed = False

    def reset(self):
        if self.flashed:
            self.energy = 0
        self.flashed = False

    def pulse(self) -> bool:
        """:returns whether the octopus flashed as a result of the pulse"""
        if self.flashed:
            return False
        self.energy += 1
        if self.energy > Octopus.MAX_ENERGY:
            self.flashed = True
        return self.flashed


class OctopusGrid:
    def __init__(self):
        self._map: Dict[Coordinate, Union[Octopus, None]] = defaultdict(lambda: None)
        self._num_rows = 0
        self._width = 0
        self.num_flashes = 0

    def add_row(self, row: str):
        self._width = len(row)
        for i in range(self._width):
            self._map[self._num_rows, i] = Octopus(int(row[i]))
        self._num_rows += 1

    def neighbouring_occupied_coords(self, pos: Coordinate) -> List[Coordinate]:
        candidates = [
            (pos[0] - 1, pos[1] - 1),
            (pos[0] - 1, pos[1]),
            (pos[0] - 1, pos[1] + 1),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0] + 1, pos[1] - 1),
            (pos[0] + 1, pos[1]),
            (pos[0] + 1, pos[1] + 1),
        ]
        return list(filter(lambda p: self._map[p] is not None, candidates))

    def flash_at(self, pos: Coordinate):
        self.num_flashes += 1
        for neighbour in self.neighbouring_occupied_coords(pos):
            if self._map[neighbour].pulse():
                self.flash_at(neighbour)

    def cycle(self) -> bool:
        """:returns whether all octopi flashed simultaneously this cycle"""
        coordinates = list(filter(lambda c: self._map[c] is not None, self._map.keys()))
        for coordinate in coordinates.copy():
            if self._map[coordinate].pulse():
                self.flash_at(coordinate)
        if all(self._map[c].flashed for c in coordinates):
            return True
        for coordinate in coordinates.copy():
            self._map[coordinate].reset()
        return False


def read_input():
    with open("11/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def run():
    run_a()
    run_b()


def parse_input() -> OctopusGrid:
    lines = read_input()
    grid = OctopusGrid()
    for line in lines:
        grid.add_row(line)
    return grid


def run_a():
    grid = parse_input()
    for _ in range(100):
        grid.cycle()
    print(grid.num_flashes)


def run_b():
    grid = parse_input()
    cycle = 0
    while True:
        cycle += 1
        if grid.cycle():
            print(cycle)
            return
