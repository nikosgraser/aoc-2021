from functools import reduce
from typing import Iterable, List, Callable


def l2s(lst: Iterable[str]) -> str:
    return reduce(lambda x, y: x + y, lst)


def b2i(bin_string: str) -> int:
    return int(f"0b{bin_string}", 0)


def invert_binary_str(b: str) -> str:
    return l2s("1" if c == "0" else "0" for c in b)


def most_common_bit(bits: Iterable[str]) -> str:
    bits = list(bits)
    return "1" if sum(1 for bit in bits if bit == "1") >= sum(1 for bit in bits if bit == "0") else "0"


def least_common_bit(bits: Iterable[str]) -> str:
    bits = list(bits)
    return "0" if sum(1 for bit in bits if bit == "1") >= sum(1 for bit in bits if bit == "0") else "1"


def ogr_strategy(numbers: List[str], index: int) -> str:
    return most_common_bit(number[index] for number in numbers)


def csr_strategy(numbers: List[str], index: int) -> str:
    return least_common_bit(number[index] for number in numbers)


def get_rating_with_strategy(numbers: List[str], strategy: Callable[[List[str], int], str]) -> str:
    for i in range(len(numbers[0])):
        target_bit = strategy(numbers, i)
        numbers = list(filter(lambda n, idx=i, tb=target_bit: n[idx] == tb, numbers))
        if len(numbers) == 1:
            return numbers[0]
    raise Exception


def read_input():
    with open("03/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def run():
    run_a()
    run_b()


def run_a():
    numbers = read_input()
    gamma = l2s(most_common_bit(number[i] for number in numbers) for i in range(len(numbers[0])))
    epsilon = invert_binary_str(gamma)
    print(b2i(gamma) * b2i(epsilon))


def run_b():
    numbers = read_input()
    ogr = get_rating_with_strategy(numbers, ogr_strategy)
    csr = get_rating_with_strategy(numbers, csr_strategy)
    print(b2i(ogr) * b2i(csr))
