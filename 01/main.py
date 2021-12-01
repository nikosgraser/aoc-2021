def read_input():
    with open("01/input.txt", "r") as fd:
        lines = fd.readlines()
    return [int(line.strip()) for line in lines]


def run():
    run_a()
    run_b()


def run_a():
    depths = read_input()
    number_of_depth_increases = sum(1 if depths[i] < depths[i + 1] else 0 for i in range(len(depths) - 1))
    print(number_of_depth_increases)


def run_b():
    depths = read_input()
    sliding_window_size = 3
    number_of_depth_increases = sum(
        1 if sum(depths[i : i + sliding_window_size]) < sum(depths[i + 1 : i + 1 + sliding_window_size]) else 0
        for i in range(len(depths) - sliding_window_size)
    )
    print(number_of_depth_increases)
