import pytest
from data import EXAMPLE, REAL
from main import get_data, part_1, part_2


@pytest.mark.parametrize(
    "func, lines, expected",
    (
        (part_1, get_data(EXAMPLE), "1588"),
        (part_2, get_data(EXAMPLE), "2188189693529"),
        (part_1, get_data(REAL), "3587"),
        (part_2, get_data(REAL), "3906445077999"),
    ),
)
def test_example(func, lines, expected):
    assert func(lines) == expected
