from __future__ import annotations

import sys

EXAMPLE_INPUT = """
199
200
208
210
200
207
240
269
260
263
"""


def part_1(lines: list[str]) -> str:
    """1553"""
    nums = list(map(int, lines))
    count = 0
    prev = nums[0]
    for n in nums[1:]:
        if n > prev:
            count += 1
        prev = n
    return str(count)


def part_2(lines: list[str]) -> str:
    """1597"""
    nums = list(map(int, lines))
    count = 0
    for i, _ in enumerate(nums[1:-1]):
        if nums[i - 1] < nums[i + 2]:
            count += 1
    return str(count)


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
