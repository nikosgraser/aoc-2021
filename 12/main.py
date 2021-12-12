from typing import Dict, List, Set, Union

START_NODE = "start"
END_NODE = "end"


class Node:
    def __init__(self, name: str):
        self.name = name
        self.neighbours: List[Node] = []
        self.is_small = self.name.islower()

    def add_neighbour(self, other):
        if other not in self.neighbours:
            self.neighbours.append(other)


class CaveGraph:
    def __init__(self):
        self._nodes: Dict[str, Node] = {}

    def _add_node(self, name: str):
        if name not in self._nodes.keys():
            self._nodes[name] = Node(name)

    def add_edge(self, name1: str, name2: str):
        self._add_node(name1)
        self._add_node(name2)
        self._nodes[name1].add_neighbour(self._nodes[name2])
        self._nodes[name2].add_neighbour(self._nodes[name1])

    @staticmethod
    def _find_paths_from(current_node: Node, visited_nodes: Set[str]) -> Union[Set[str], None]:
        if current_node.name == END_NODE:
            return {END_NODE}
        valid_paths: Set[str] = set()
        for neighbour in filter(lambda n: n.name not in visited_nodes, current_node.neighbours):
            paths = CaveGraph._find_paths_from(
                neighbour, visited_nodes | {current_node.name} if current_node.is_small else visited_nodes
            )
            valid_paths |= {current_node.name + path for path in paths} if paths is not None else set()
        return valid_paths or None

    @staticmethod
    def _find_paths_with_double_visit_from(
        current_node: Node, visited_nodes: Set[str], double_visit_available: bool
    ) -> Union[Set[str], None]:
        if current_node.name == END_NODE:
            return {END_NODE}
        valid_paths: Set[str] = set()
        for neighbour in filter(lambda n: n.name not in visited_nodes, current_node.neighbours):
            if double_visit_available and current_node.is_small:
                paths = CaveGraph._find_paths_with_double_visit_from(neighbour, visited_nodes, False)
                valid_paths |= {current_node.name + path for path in paths} if paths is not None else set()
            paths = CaveGraph._find_paths_with_double_visit_from(
                neighbour,
                visited_nodes | {current_node.name} if current_node.is_small else visited_nodes,
                double_visit_available,
            )
            valid_paths |= {current_node.name + path for path in paths} if paths is not None else set()
        return valid_paths or None

    def find_all_paths(self, double_visit_allowed: bool) -> Set[str]:
        if double_visit_allowed:
            return CaveGraph._find_paths_with_double_visit_from(self._nodes[START_NODE], {START_NODE}, True)
        return CaveGraph._find_paths_from(self._nodes[START_NODE], set())


def read_input():
    with open("12/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def run():
    run_a()
    run_b()


def parse_input() -> CaveGraph:
    graph = CaveGraph()
    lines = read_input()
    for line in lines:
        nodes = line.split("-")
        graph.add_edge(nodes[0], nodes[1])
    return graph


def run_a():
    graph = parse_input()
    print(len(graph.find_all_paths(double_visit_allowed=False)))


def run_b():
    graph = parse_input()
    print(len(graph.find_all_paths(double_visit_allowed=True)))
