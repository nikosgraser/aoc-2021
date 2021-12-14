from collections import defaultdict
from typing import Dict, Tuple


def read_input():
    with open("14/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def run():
    run_a()
    run_b()


def parse_input() -> Tuple[str, Dict[str, str]]:
    lines = read_input()
    polymer_template: str = lines[0]
    insertion_rules: Dict[str, str] = defaultdict(
        str, {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines[2:]}
    )
    return polymer_template, insertion_rules


def apply_rules(start_sequence: str, rules: Dict[str, str]):
    modified_sequence = ""
    for i in range(len(start_sequence) - 1):
        modified_sequence += start_sequence[i] + rules[start_sequence[i] + start_sequence[i + 1]]
    return modified_sequence + start_sequence[-1]


def frequency_analysis_from_str(sequence: str) -> int:
    character_counts = {c: sequence.count(c) for c in set(sequence)}
    most_frequent_character = max(character_counts.keys(), key=lambda c: character_counts[c])
    least_frequent_character = min(character_counts.keys(), key=lambda c: character_counts[c])
    return character_counts[most_frequent_character] - character_counts[least_frequent_character]


def frequency_analysis_from_dict(pair_counts: Dict[str, int], last_char: str) -> int:
    character_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        character_counts[pair[0]] += count
    character_counts[last_char] += 1
    most_frequent_character = max(character_counts.keys(), key=lambda c: character_counts[c])
    least_frequent_character = min(character_counts.keys(), key=lambda c: character_counts[c])
    return character_counts[most_frequent_character] - character_counts[least_frequent_character]


def run_a():
    polymer, insertion_rules = parse_input()
    for _ in range(10):
        polymer = apply_rules(polymer, insertion_rules)
    print(frequency_analysis_from_str(polymer))


def run_b():
    polymer_template, insertion_rules = parse_input()
    pair_counts: Dict[str, int] = defaultdict(int)
    for i in range(len(polymer_template) - 1):
        pair_counts[polymer_template[i] + polymer_template[i + 1]] += 1
    for _ in range(40):
        next_pair_counts: Dict[str, int] = defaultdict(int)
        for pair, count in pair_counts.items():
            next_pair_counts[pair[0] + insertion_rules[pair]] += count
            next_pair_counts[insertion_rules[pair] + pair[1]] += count
        pair_counts = next_pair_counts
    print(frequency_analysis_from_dict(pair_counts, polymer_template[-1]))
