from __future__ import annotations

import sys

EXAMPLE_INPUT = """
"""


def part_1(lines: list[str]) -> str:
    return ""


def part_2(lines: list[str]) -> str:
    return ""


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
