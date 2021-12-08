from pathlib import Path

import pytest
from main import get_input, part_1, part_2

INPUT_PATH = str(Path(__file__).parent / "input.txt")


@pytest.mark.parametrize(
    "func, lines, expected",
    (
        (part_1, get_input(), "26"),
        (part_2, get_input(), "61229"),
        (part_1, get_input(INPUT_PATH), "548"),
        (part_2, get_input(INPUT_PATH), "1074888"),
    ),
)
def test_example(func, lines, expected):
    assert func(lines) == expected
