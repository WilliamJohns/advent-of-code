import sys

EXAMPLE_INPUT = """3,4,3,1,2"""


def suck_it_darwin(stupid_fish, days):
    spawn_groups = [0] * 9
    for fish in stupid_fish:
        spawn_groups[fish] += 1

    for day in range(days):
        spawning = spawn_groups[0]
        for i in range(8):
            spawn_groups[i] = spawn_groups[i + 1]
        spawn_groups[8] = spawning
        spawn_groups[6] += spawning

    return sum(spawn_groups)


def part_1(lines):
    """350149"""
    stupid_fish = list(map(int, lines[0].split(",")))
    return suck_it_darwin(stupid_fish, 80)


def part_2(lines):
    stupid_fish = list(map(int, lines[0].split(",")))
    return suck_it_darwin(stupid_fish, 256)


def get_input(file_path=None):
    """1590327954513"""
    if len(sys.argv) == 2 or file_path is not None:
        fp = file_path or sys.argv[1]
        with open(fp) as f:
            lines = [line.strip() for line in f.readlines()]
    else:
        lines = [line.strip() for line in EXAMPLE_INPUT.split("\n")]
    return lines


def main():
    lines = get_input()

    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
