from collections import defaultdict


def part_1(lines) -> None:
    """6461"""
    vent_map = defaultdict(int)
    for line in lines:
        start, stop = line.split(" -> ")
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, stop.split(","))
        if x1 == x2:
            y0 = min(y1, y2)
            for dy in range(abs(y1-y2)+1):
                vent_map[(x1, dy+y0)] += 1
        elif y1 == y2:
            x0 = min(x1, x2)
            for dx in range(abs(x1-x2)+1):
                vent_map[(x0+dx, y1)] += 1
        

    print(len([
        1
        for v in vent_map.values()
        if v > 1
    ]))

def part_2(lines) -> None:
    """18065"""
    vent_map = defaultdict(int)
    for line in lines:
        start, stop = line.split(" -> ")
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, stop.split(","))
        if x1 == x2:
            y0 = min(y1, y2)
            for dy in range(abs(y1-y2)+1):
                vent_map[(x1, dy+y0)] += 1
        elif y1 == y2:
            x0 = min(x1, x2)
            for dx in range(abs(x1-x2)+1):
                vent_map[(x0+dx, y1)] += 1
        elif abs(x1-x2) == abs(y1-y2):
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            for i in range(abs(x2-x1)+1):
                xi = x1 + (dx*i)
                yi = y1 + (dy*i)
                vent_map[(xi, yi)] += 1

    print(len([
        1
        for v in vent_map.values()
        if v > 1
    ]))


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

