from __future__ import annotations

from heapq import heappop, heappush
from math import sqrt

from data import EXAMPLE, REAL  # noqa: F401


def compute(tile: list[int], size: int = 1) -> int:
    tile_width = int(sqrt(len(tile)))
    tile_height = tile_width

    width = tile_width * size
    height = tile_height * size
    start = (0, 0)
    dest = (height - 1, width - 1)

    seen = {start}
    nodes = [(0, *start)]
    while nodes:
        dist, y, x = heappop(nodes)
        if (y, x) == dest:
            return dist

        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            yi = y + dy
            xi = x + dx

            if xi < 0 or yi < 0 or xi >= width or yi >= height or (yi, xi) in seen:
                continue

            seen.add((yi, xi))
            y_tile, y_mod = divmod(yi, tile_height)
            x_tile, x_mod = divmod(xi, tile_width)
            tile_idx = (y_mod * tile_width) + x_mod
            neighbor_dist = (tile[tile_idx] + y_tile + x_tile - 1) % 9 + 1

            heappush(nodes, (neighbor_dist + dist, yi, xi))
    return -1


def part_1(data: list[int]) -> int:
    """717"""
    return compute(data, 1)


def part_2(data: list[int]) -> int:
    """2993"""
    return compute(data, 5)


def get_data(data: str) -> list[int]:
    return list(map(int, data.replace("\n", "")))


def main():
    # data = get_data(EXAMPLE)
    data = get_data(REAL)

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
