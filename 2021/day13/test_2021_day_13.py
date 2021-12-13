import pytest
from data import EXAMPLE, REAL
from main import parse_data, part_1, part_2

EXAMPLE_PART_1 = """\
#####
#...#
#...#
#...#
#####
.....
....."""

REAL_PART_2 = """\
.##..####...##.#..#.#....#..#..##....##.
#..#.#.......#.#.#..#....#..#.#..#....#.
#....###.....#.##...#....#..#.#.......#.
#....#.......#.#.#..#....#..#.#.##....#.
#..#.#....#..#.#.#..#....#..#.#..#.#..#.
.##..####..##..#..#.####..##...###..##.."""


@pytest.mark.parametrize(
    "func, lines, expected",
    (
        (part_1, parse_data(EXAMPLE), "17"),
        (part_2, parse_data(EXAMPLE), EXAMPLE_PART_1),
        (part_1, parse_data(REAL), "795"),
        (part_2, parse_data(REAL), REAL_PART_2),
    ),
)
def test_example(func, lines, expected):
    assert func(lines) == expected
