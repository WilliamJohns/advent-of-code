from __future__ import annotations

import sys

EXAMPLE_INPUT = """\
16,1,2,0,4,2,7,1,2,14
"""


def part_1(lines: list[str]) -> str:
    """353800"""
    crabs = list(map(int, lines[0].split(",")))
    min_fuel = None
    max_crab = max(crabs)

    for dest in range(max_crab):
        fuel_cost = sum([abs(dest - crab) for crab in crabs])
        if min_fuel is None or fuel_cost < min_fuel:
            min_fuel = fuel_cost

    return str(min_fuel)


def part_2(lines: list[str]) -> str:
    """98119739"""
    crabs = list(map(int, lines[0].split(",")))
    min_fuel = None
    max_crab = max(crabs)
    triangle_numbers = []
    acc = 0
    for i in range(max_crab + 1):
        triangle_numbers.append(acc := acc + i)

    for dest in range(max_crab):
        fuel_cost = sum([triangle_numbers[abs(crab - dest)] for crab in crabs])
        if min_fuel is None or fuel_cost < min_fuel:
            min_fuel = fuel_cost

    return str(min_fuel)


def get_input(file_path: str | None = None) -> list[str]:
    if len(sys.argv) == 2 or file_path is not None:
        fp = file_path or sys.argv[1]
        with open(fp) as f:
            lines = [line.strip() for line in f.readlines()]
    else:
        lines = [line.strip() for line in EXAMPLE_INPUT.split("\n")]
    return lines


def main() -> None:
    lines = get_input()

    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
