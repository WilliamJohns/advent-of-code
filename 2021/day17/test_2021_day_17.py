import pytest
from data import EXAMPLE, REAL
from main import get_data, part_1, part_2


@pytest.mark.parametrize(
    "func, lines, expected",
    (
        (part_1, get_data(EXAMPLE), 45),
        (part_2, get_data(EXAMPLE), 112),
        (part_1, get_data(REAL), 25200),
        (part_2, get_data(REAL), 3012),
    ),
)
def test_example(func, lines, expected):
    assert func(lines) == expected
