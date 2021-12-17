from __future__ import annotations

from data import EXAMPLE, REAL  # noqa: F401


def simulate_launch(x: int, y: int, target_area: tuple[int, int, int, int]) -> bool:
    x_travel = 0
    y_travel = 0
    x_min, x_max, y_min, y_max = target_area
    while True:
        x_travel += x
        y_travel += y
        x = max(x - 1, 0)
        y -= 1
        if x_min <= x_travel <= x_max and y_min <= y_travel <= y_max:
            return True
        if y_travel < y_min:
            return False


def part_1(data: str) -> int:
    _, ypart = data.split(":")
    min_y, _ = map(int, ypart.split(","))

    max_y_velcocity = abs(min_y) - 1
    return max_y_velcocity * (max_y_velcocity + 1) // 2


def part_2(data: str) -> int:
    xpart, ypart = data.split(":")
    min_x, max_x = map(int, xpart.split(","))
    min_y, max_y = map(int, ypart.split(","))

    valid = set()
    area = (min_x, max_x, min_y, max_y)
    for x in range(max_x + 1):
        for y in range(min_y, min_y * -1):
            if simulate_launch(x, y, area):
                valid.add((x, y))
    return len(valid)


def get_data(data) -> str:
    return data.replace("target area: x=", "").replace(", y=", ":").replace("..", ",")


def main() -> None:
    # lines = get_data(EXAMPLE)
    lines = get_data(REAL)

    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
