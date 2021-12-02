def read_input():
    with open("02/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip().split() for line in lines]


def run():
    run_a()
    run_b()


def run_a():
    instructions = read_input()
    pos_horizontal, pos_vertical = 0, 0
    for instruction in instructions:
        if instruction[0] == "forward":
            pos_horizontal += int(instruction[1])
        elif instruction[0] == "down":
            pos_vertical += int(instruction[1])
        elif instruction[0] == "up":
            pos_vertical -= int(instruction[1])
    print(pos_horizontal * pos_vertical)


def run_b():
    instructions = read_input()
    pos_horizontal, pos_vertical, aim = 0, 0, 0
    for instruction in instructions:
        if instruction[0] == "forward":
            pos_horizontal += int(instruction[1])
            pos_vertical += int(instruction[1]) * aim
        elif instruction[0] == "down":
            aim += int(instruction[1])
        elif instruction[0] == "up":
            aim -= int(instruction[1])
    print(pos_horizontal * pos_vertical)
