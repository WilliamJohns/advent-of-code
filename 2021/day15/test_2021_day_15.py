import pytest
from data import EXAMPLE, REAL
from main import get_data, part_1, part_2


@pytest.mark.parametrize(
    "func, data, expected",
    (
        (part_1, get_data(EXAMPLE), 40),
        (part_2, get_data(EXAMPLE), 315),
        (part_1, get_data(REAL), 717),
        (part_2, get_data(REAL), 2993),
    ),
)
def test_example(func, data, expected):
    assert func(data) == expected
