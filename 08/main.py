from functools import reduce
from typing import Dict, List, Set, FrozenSet


def read_input():
    with open("08/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


DIGITS_BY_SEGMENTS: Dict[FrozenSet[str], str] = {
    frozenset({"a", "b", "c", "e", "f", "g"}): "0",
    frozenset({"c", "f"}): "1",
    frozenset({"a", "c", "d", "e", "g"}): "2",
    frozenset({"a", "c", "d", "f", "g"}): "3",
    frozenset({"b", "c", "d", "f"}): "4",
    frozenset({"a", "b", "d", "f", "g"}): "5",
    frozenset({"a", "b", "d", "e", "f", "g"}): "6",
    frozenset({"a", "c", "f"}): "7",
    frozenset({"a", "b", "c", "d", "e", "f", "g"}): "8",
    frozenset({"a", "b", "c", "d", "f", "g"}): "9",
}


def run():
    run_a()
    run_b()


def run_a():
    lines = read_input()
    outputs = [line.split("|")[1].strip().split() for line in lines]
    flat_outputs = [num for output in outputs for num in output]
    special_digit_numbers = [2, 3, 4, 7]
    print(sum(1 for num in flat_outputs if len(num) in special_digit_numbers))


def value_by_len(values: List[str], length: int) -> Set[str]:
    return set(values_by_len(values, length).pop())


def values_by_len(values: List[str], length: int) -> Set[str]:
    return {v for v in values if len(v) == length}


def get_wiring(values: List[str]) -> Dict[str, str]:
    one = value_by_len(values, 2)
    four = value_by_len(values, 4)
    seven = value_by_len(values, 3)
    eight = value_by_len(values, 7)
    wiring_reverse: Dict[str, str] = {}
    cf = one
    acf = seven
    wiring_reverse["a"] = (acf - cf).pop()
    len6 = values_by_len(values, 6)
    six = {s for s in [v for v in len6 if not set(v) > cf][0]}
    wiring_reverse["c"] = (eight - six).pop()
    wiring_reverse["f"] = (cf - set(wiring_reverse["c"])).pop()
    zero_nine = {v for v in len6 if set(v) != six}
    zn1, zn2 = zero_nine.pop(), zero_nine.pop()
    de = {(set(zn1) - set(zn2)).pop(), (set(zn2) - set(zn1)).pop()}
    wiring_reverse["d"] = (de & four).pop()
    wiring_reverse["e"] = (de - set(wiring_reverse["d"])).pop()
    wiring_reverse["b"] = (four - cf - set(wiring_reverse["d"])).pop()
    wiring_reverse["g"] = {v for v in eight if v not in wiring_reverse.values()}.pop()
    return {v: k for k, v in wiring_reverse.items()}


def digit_by_wiring(val: str, wiring: Dict[str, str]) -> str:
    rewired = {wiring[v] for v in val}
    return DIGITS_BY_SEGMENTS[frozenset(rewired)]


def run_b():
    lines = read_input()
    cumulative_value = 0
    for line in lines:
        values_and_outputs = line.split("|")
        values = values_and_outputs[0].strip().split()
        outputs = values_and_outputs[1].strip().split()
        wiring = get_wiring(values)
        output_digits = [digit_by_wiring(value, wiring) for value in outputs]
        cumulative_value += int(reduce(lambda x, y: x + y, output_digits))
    print(cumulative_value)
