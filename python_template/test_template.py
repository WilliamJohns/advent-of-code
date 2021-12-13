import pytest
from data import EXAMPLE, REAL
from main import get_lines, part_1, part_2


@pytest.mark.parametrize(
    "func, lines, expected",
    (
        (part_1, get_lines(EXAMPLE), ""),
        (part_2, get_lines(EXAMPLE), ""),
        (part_1, get_lines(REAL), ""),
        (part_2, get_lines(REAL), ""),
    ),
)
def test_example(func, lines, expected):
    assert func(lines) == expected
