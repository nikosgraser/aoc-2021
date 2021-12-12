from typing import List, Dict

CHUNK_BORDERS: Dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
CHUNK_BORDERS_REVERSE = {v: k for k, v in CHUNK_BORDERS.items()}
CORRUPTED_SCORES: Dict[str, int] = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
INCOMPLETE_SCORES: Dict[str, int] = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def read_input():
    with open("10/input.txt", "r") as fd:
        lines = fd.readlines()
    return [line.strip() for line in lines]


def run():
    run_a()
    run_b()


def incomplete_line_score(line: str) -> int:
    stack: List[str] = []
    for c in line:
        if c in CHUNK_BORDERS.keys():
            stack.append(c)
        else:
            stack.pop()
    closing_sequence = map(lambda x: CHUNK_BORDERS[x], reversed(stack))
    line_score = 0
    for c in closing_sequence:
        line_score *= 5
        line_score += INCOMPLETE_SCORES[c]
    return line_score


def corrupted_line_score(line: str) -> int:
    stack: List[str] = []
    for c in line:
        if c in CHUNK_BORDERS.keys():
            stack.append(c)
        else:
            if stack.pop() != CHUNK_BORDERS_REVERSE[c]:
                return CORRUPTED_SCORES[c]
    return 0


def run_a():
    lines = read_input()
    score = 0
    for line in lines:
        score += corrupted_line_score(line)
    print(score)


def run_b():
    lines = read_input()
    scores = []
    for line in lines:
        if corrupted_line_score(line) > 0:
            continue
        scores.append(incomplete_line_score(line))
    scores.sort()
    print(scores[len(scores) // 2])
