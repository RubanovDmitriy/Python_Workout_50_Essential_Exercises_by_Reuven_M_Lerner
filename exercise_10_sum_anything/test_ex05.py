import pytest

from exercise_10_sum_anything.exercise_10_mysum_bigger_than import mysum_bigger_than
from exercise_10_sum_anything.exercise_10_sum_anything import mysum
from exercise_10_sum_anything.exercise_10_sum_numeric import sum_numeric


@pytest.mark.parametrize(('argumets', 'output'), [
    (('abc', 'def'), 'abcdef'),
    (([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),
    ((1, 2, 3), 6),
    ((), ())
])
def test_mysum(argumets, output):
    assert mysum(*argumets) == output


def test_mysum_bigger_than():
    assert mysum_bigger_than(10, 5, 20, 30, 6) == 50


def test_sum_numeric():
    assert sum_numeric(10, 20, 'a', '30', 'bcd') == 60
