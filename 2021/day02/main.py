def part_1(lines) -> None:
    """1690020"""
    x, y = 0, 0
    for line in lines:
        direction, val = line.split()
        val = int(val)

        if direction == "forward":
            x += val
        if direction == "down":
            y += val
        if direction == "up":
            y -= val

    print(x*y)


def part_2(lines) -> None:
    """1408487760"""
    x, y = 0, 0
    aim = 0
    for line in lines:
        direction, val = line.split()
        val = int(val)

        if direction == "forward":
            x += val
            y += aim*val
        if direction == "down":
            aim += val
        if direction == "up":
            aim -= val

    print(x*y)

def main():
    with open("input.txt", "r") as f:
        lines = [
            line.strip()
            for line in f.readlines()
        ]

    part_1(lines)
    part_2(lines)


if __name__ == "__main__":
    main()

