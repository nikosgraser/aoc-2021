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
    """When the direct modeling no longer scales, we need to kill each fish's individuality :("""
    school = parse_input()
    fish_by_timer: Dict[int, int] = {timer: 0 for timer in range(Lanternfish.cycling_time_young)}
    for fish in school.fish:
        fish_by_timer[fish.timer] += 1
    for _ in range(256):
        fish_that_spawn = fish_by_timer[0]
        fish_by_timer = {
            timer: fish_by_timer[(timer + 1) % Lanternfish.cycling_time_young]
            for timer in range(Lanternfish.cycling_time_young)
        }
        fish_by_timer[Lanternfish.cycling_time - 1] += fish_that_spawn
    print(sum(fish_by_timer.values()))
