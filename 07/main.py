from typing import List, Callable


def read_input():
    with open("07/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def median(nums: List[int]) -> int:
    nums_sorted = sorted(nums)
    return nums_sorted[len(nums) // 2]


def cumulative_fuel_cost(pos: int, numbers: List[int]) -> int:
    return sum(sum(range(abs(pos - num) + 1)) for num in numbers)


def discrete_descend(start_x: int, func: Callable) -> int:
    current_x = start_x
    v_down, v_curr, v_up = func(current_x - 1), func(current_x), func(current_x + 1)
    if min(v_down, v_curr, v_up) == v_curr:
        return current_x
    step = -1 if v_down < v_curr else 1
    while True:
        next_x = current_x + step
        if func(next_x) > func(current_x):
            return current_x
        current_x = next_x


def run():
    run_a()
    run_b()


def run_a():
    numbers = list(map(int, read_input()[0].split(",")))
    med = median(numbers)
    print(sum(abs(med - num) for num in numbers))


def run_b():
    numbers = list(map(int, read_input()[0].split(",")))
    optimum = discrete_descend(median(numbers), lambda x: cumulative_fuel_cost(x, numbers))
    print(cumulative_fuel_cost(optimum, numbers))
