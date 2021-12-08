from __future__ import annotations

import sys

EXAMPLE_INPUT = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


def part_1(lines: list[str]) -> str:
    """548"""
    count = 0
    for line in lines:
        a, b = line.split(" | ")
        for signal in b.split():
            if len(signal) in {2, 3, 4, 7}:
                count += 1
    return str(count)


def part_2(lines: list[str]) -> str:
    """1074888"""
    nums = []
    for line in lines:
        a, b = line.split(" | ")
        unknown_signals = a.split() + b.split()
        fail_set = {"h"}
        known_signals: dict[int, set[str]] = {}
        while len(known_signals) < 10:
            for signal in unknown_signals:
                signal_length = len(signal)
                signal_set = set(signal)

                if signal_length == 2:
                    known_signals[1] = signal_set
                elif signal_length == 3:
                    known_signals[7] = signal_set
                elif signal_length == 4:
                    known_signals[4] = signal_set
                elif signal_length == 7:
                    known_signals[8] = signal_set
                elif signal_length == 6:
                    if signal_set.issuperset(known_signals.get(4, fail_set)):
                        known_signals[9] = signal_set
                    elif signal_set.issuperset(known_signals.get(1, fail_set)):
                        known_signals[0] = signal_set
                    elif 1 in known_signals and 4 in known_signals:
                        known_signals[6] = signal_set
                elif signal_length == 5:
                    if signal_set.issuperset(known_signals.get(1, fail_set)):
                        known_signals[3] = signal_set
                    elif signal_set.issubset(known_signals.get(6, fail_set)):
                        known_signals[5] = signal_set
                    elif 6 in known_signals and 1 in known_signals:
                        known_signals[2] = signal_set

        translation_map = {"".join(sorted(v)): str(k) for k, v in known_signals.items()}
        num = ""
        for signal in b.split():
            key = "".join(sorted(signal))
            num += translation_map[key]
        nums.append(int(num))

    return str(sum(nums))


def get_input(file_path: str | None = None) -> list[str]:
    if len(sys.argv) == 2 or file_path is not None:
        fp = file_path or sys.argv[1]
        with open(fp) as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    else:
        lines = [line.strip() for line in EXAMPLE_INPUT.split("\n") if line.strip()]
    return lines


def main() -> None:
    lines = get_input()

    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
