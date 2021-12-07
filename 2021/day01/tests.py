from pathlib import Path

import pytest
from main import get_input, part_1, part_2

INPUT_PATH = str(Path(__file__).parent / "input.txt")


@pytest.mark.parametrize(
    "func, lines, expected",
    (
        (part_1, get_input(), "7"),
        (part_2, get_input(), "5"),
        (part_1, get_input(INPUT_PATH), "1553"),
        (part_2, get_input(INPUT_PATH), "1597"),
    ),
)
def test_example(func, lines, expected):
    assert func(lines) == expected
