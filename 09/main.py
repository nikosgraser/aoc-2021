from collections import defaultdict
from typing import Dict, Tuple, List

Coordinate = Tuple[int, int]


class Point:
    def __init__(self, pos: Coordinate, value: int):
        self.pos = pos
        self.value = value

    def __eq__(self, other):
        return self.pos == other.pos and self.value == other.value

    def neighbouring_coords(self) -> List[Coordinate]:
        return [
            (self.pos[0] - 1, self.pos[1]),
            (self.pos[0] + 1, self.pos[1]),
            (self.pos[0], self.pos[1] - 1),
            (self.pos[0], self.pos[1] + 1),
        ]


class Heightmap:
    def __init__(self):
        self._map: Dict[Coordinate, int] = defaultdict(lambda: 10)
        self._num_rows = 0
        self._width = 0

    def add_row(self, row: str):
        self._width = len(row)
        for i in range(self._width):
            self._map[self._num_rows, i] = int(row[i])
        self._num_rows += 1

    def get_low_point_heights(self) -> List[int]:
        return [point.value for point in self.get_low_points()]

    def get_low_points(self) -> List[Point]:
        low_points: List[Point] = []
        coordinates = list(filter(lambda c: 0 <= c[0] < self._num_rows and 0 <= c[1] < self._width, self._map.keys()))
        for i, j in coordinates.copy():
            neighbouring_values = [self._map[x, y] for x, y in Point((i, j), 0).neighbouring_coords()]
            if all(neighbour_val > self._map[i, j] for neighbour_val in neighbouring_values):
                low_points.append(Point((i, j), self._map[i, j]))
        return low_points

    def get_basin_for_low_point(self, low_point: Point) -> List[Point]:
        processing = [low_point]
        basin = [low_point]
        while len(processing) > 0:
            current = processing.pop()
            neighbours = [Point((i, j), self._map[i, j]) for i, j in current.neighbouring_coords()]
            for n in neighbours:
                if n not in processing and n not in basin and n.value < 9:
                    processing.append(n)
                    basin.append(n)
        return basin

    def get_basins(self) -> List[List[Point]]:
        basins: List[List[Point]] = []
        for low_point in self.get_low_points():
            basins.append(self.get_basin_for_low_point(low_point))
        return basins


def read_input():
    with open("09/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def run():
    run_a()
    run_b()


def run_a():
    hm = Heightmap()
    for line in read_input():
        hm.add_row(line)
    print(sum(1 + val for val in hm.get_low_point_heights()))


def run_b():
    hm = Heightmap()
    for line in read_input():
        hm.add_row(line)
    basins = hm.get_basins()
    basins.sort(key=lambda b: len(b), reverse=True)
    print(len(basins[0]) * len(basins[1]) * len(basins[2]))
