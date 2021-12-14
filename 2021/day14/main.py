from __future__ import annotations

from collections import defaultdict

from data import EXAMPLE, REAL  # noqa: F401


def compute(polymer: str, rules: dict[str, str], steps: int) -> int:
    pair_counts: dict[str, int] = defaultdict(int)
    for i in range(len(polymer) - 1):
        pair_counts[polymer[i : i + 2]] += 1

    for _ in range(steps):
        new_pair_counts: dict[str, int] = defaultdict(int)
        for pair, count in pair_counts.items():
            split = rules.get(pair, "")
            new_pair_counts[pair[0] + split] += count
            new_pair_counts[split + pair[1]] += count
        pair_counts = new_pair_counts

    letter_counts: dict[str, int] = defaultdict(int)
    for pair, count in pair_counts.items():
        letter_counts[pair[0]] += count
    letter_counts[polymer[-1]] += 1

    ch_min = min(letter_counts.values())
    ch_max = max(letter_counts.values())

    return ch_max - ch_min


def part_1(data) -> str:
    """3587"""
    polymer = data["template"]
    rules = data["rules"]

    return str(compute(polymer, rules, 10))


def part_2(data) -> str:
    """3906445077999"""
    polymer = data["template"]
    rules = data["rules"]

    return str(compute(polymer, rules, 40))


def get_data(data):
    template, *rules = data.split("\n")
    rule_dict = {}
    for rule in rules:
        match, split = rule.split(" -> ")
        rule_dict[match] = split

    return {"template": template, "rules": rule_dict}


def main() -> None:
    # lines = get_data(EXAMPLE)
    data = get_data(REAL)
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
