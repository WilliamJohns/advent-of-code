from __future__ import annotations

import sys

EXAMPLE_INPUT = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


def part_1(lines: list[str]) -> str:
    """436497"""
    POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
    PAIRS = {
        "(": ")",
        "{": "}",
        "<": ">",
        "[": "]",
    }
    score = 0
    for line in lines:
        opens = []
        for ch in line:
            if ch not in POINTS:
                opens.append(ch)
            elif PAIRS[opens[-1]] == ch:
                opens.pop(-1)
            else:
                score += POINTS[ch]
                break
    return str(score)


def part_2(lines: list[str]) -> str:
    """2377613374"""
    POINTS = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    PAIRS = {
        "(": ")",
        "{": "}",
        "<": ">",
        "[": "]",
    }
    scores = []
    for line in lines:
        total = 0
        opens = []
        corrupt = False
        for ch in line:
            if ch not in POINTS:
                opens.append(ch)
            elif PAIRS[opens[-1]] == ch:
                opens.pop(-1)
            else:
                corrupt = True
                break
        if not corrupt:
            for ch in reversed(opens):
                match = PAIRS[ch]
                total *= 5
                total += POINTS[match]
            scores.append(total)

    scores.sort()
    return str(scores[len(scores) // 2])


def get_input(file_path: str | None = None) -> list[str]:
    if len(sys.argv) == 2 or file_path is not None:
        fp = file_path or sys.argv[1]
        with open(fp) as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    else:
        lines = [line.strip() for line in EXAMPLE_INPUT.split("\n") if line.strip()]
    return lines


def main() -> None:
    lines = get_input()

    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
