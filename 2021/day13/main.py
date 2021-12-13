from __future__ import annotations

from typing import Any

from data import EXAMPLE, REAL  # noqa: F401


class Oragami:
    def __init__(self, dots: list[tuple[int, int]]):
        self.width = max(x for x, _ in dots) + 1
        self.height = max(y for _, y in dots) + 1
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for x, y in dots:
            self.grid[y][x] = 1

    def __str__(self) -> str:
        s = []
        for row in self.grid:
            s.append(
                "".join(
                    map(
                        lambda x: "#" if x == 1 else ".",
                        row,
                    )
                )
            )
        return "\n".join(s)

    @property
    def dot_count(self) -> int:
        return sum(sum(row) for row in self.grid)

    def fold(self, axis: str, divider: int) -> None:
        if axis == "y":
            start = self.height // 2
            for offset, row in enumerate(self.grid[start + 1 :]):
                ry = (start - 1) - offset
                for x, i in enumerate(row):
                    self.grid[ry][x] = i | self.grid[ry][x]
            self.grid = self.grid[:start]
            self.height = start

        else:
            start = self.width // 2
            for y, row in enumerate(self.grid):
                for offset, i in enumerate(row[start + 1 :]):
                    rx = (start - 1) - offset
                    self.grid[y][rx] = i | self.grid[y][rx]
                self.grid[y] = row[:start]
            self.width = start


def part_1(data: dict[str, list[Any]]) -> str:
    """795"""
    oragami = Oragami(data["dots"])
    first_fold = data["folds"][0]
    axis, val = first_fold.split("=")
    val = int(val)
    oragami.fold(axis, val)

    return str(oragami.dot_count)


def part_2(data: dict[str, list[Any]]) -> str:
    """CEJKLUGJ"""
    oragami = Oragami(data["dots"])
    for fold in data["folds"]:
        axis, val = fold.split("=")
        val = int(val)
        oragami.fold(axis, val)

    return str(oragami)


def parse_data(data) -> dict[str, list[Any]]:
    dots, *folds = data.split("fold along ")
    data = {
        "dots": [tuple(map(int, coord.split(","))) for coord in dots.split()],
        "folds": [fold.strip() for fold in folds],
    }
    return data


def main() -> None:
    # lines = parse_data(EXAMPLE)
    lines = parse_data(REAL)

    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
