from collections import defaultdict


def part_1(lines) -> None:
    """3277364"""
    counts = defaultdict(lambda: defaultdict(int))
    for line in lines:
        for idx, bit in enumerate(map(int, line)):
            counts[idx][bit] += 1

    gamma = ""
    epsilon = ""
    for count in counts.values():
        gamma += "1" if count[1] > count[0] else "0"
        epsilon += "1" if count[1] < count[0] else "0"

    print(int(gamma, 2)*int(epsilon, 2))

def part_2(lines) -> None:
    """5736383"""
    ox = list(lines)
    carb = list(lines)
    col = 0
    while len(ox) > 1 and len(carb) > 0:
        if len(ox) > 1:
            zeroes = len([
                1
                for line in ox
                if line[col] == "0"
            ])
            ones = len(ox) - zeroes
            check = "1" if ones >= zeroes else "0"
            ox = [
                line
                for line in ox
                if line[col] == check
            ]

        if len(carb) > 1:
            zeroes = len([
                1
                for line in carb
                if line[col] == "0"
            ])
            ones = len(carb) - zeroes
            check = "1" if ones < zeroes else "0"
            carb = [
                line
                for line in carb
                if line[col] == check
            ]

        col += 1

    ox = ox[0]
    carb = carb[0]
    print(int(ox, 2) * int(carb, 2))

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

