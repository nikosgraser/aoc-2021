from typing import List, Dict


class LanternfishSchool:
    def __init__(self):
        self.fish: List[Lanternfish] = []

    def __len__(self):
        return len(self.fish)

    def add_fish(self, initial_timer):
        self.fish.append(Lanternfish(initial_timer, self))

    def cycle(self):
        current_fish = self.fish.copy()
        for fish in current_fish:
            fish.cycle()


class Lanternfish:
    cycling_time = 7
    cycling_time_young = 9

    def __init__(self, timer: int, school: LanternfishSchool):
        self.timer = timer
        self.school = school

    def cycle(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = Lanternfish.cycling_time - 1
            self.school.add_fish(Lanternfish.cycling_time_young - 1)


def read_input():
    with open("06/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def parse_input() -> LanternfishSchool:
    lines = read_input()
    school = LanternfishSchool()
    initial_fish_timers = map(int, lines[0].split(","))
    for timer in initial_fish_timers:
        school.add_fish(timer)
    return school


def run():
    run_a()
    run_b()


def run_a():
    """This is the fun part where you get to model the fishies nicely"""
    school = parse_input()
    for _ in range(80):
        school.cycle()
    print(len(school))


def run_b():
    """When the direct modeling no longer scales, we need to kill each fish's indiduality :("""
    school = parse_input()
    fish_by_age: Dict[int, int] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in school.fish:
        fish_by_age[fish.timer] += 1
    for _ in range(256):
        next_fish_by_age: Dict[int, int] = {8: fish_by_age[0], 7: fish_by_age[8], 6: fish_by_age[7] + fish_by_age[0]}
        for i in range(6):
            next_fish_by_age[i] = fish_by_age[i + 1]
        fish_by_age = next_fish_by_age
    print(sum(v for k, v in fish_by_age.items()))
