from __future__ import annotations

from data import EXAMPLE, REAL  # noqa: F401


def part_1(lines: list[str]) -> str:
    return ""


def part_2(lines: list[str]) -> str:
    return ""


def get_lines(data) -> list[str]:
    return [line.strip() for line in data.split("\n") if line.strip()]


def main() -> None:
    lines = get_lines(EXAMPLE)
    # lines = get_lines(REAL)

    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
