import pytest

from exercise_09_first_last.excercise_09_plus_minus import plus_minus
from exercise_09_first_last.exercise_09_even_odd_sum import even_odd_sums
from exercise_09_first_last.exercise_09_first_last import firstlast


@pytest.mark.parametrize(('sequence', 'output'), [
    ('abc', 'ac'),
    ([1, 2, 3, 4], [1, 4]),
    ((1, 2, 3, 4), (1, 4)),
    ('c', 'cc'),
    ([2], [2, 2])
])
def test_firstlast(sequence, output):
    assert firstlast(sequence) == output


@pytest.mark.parametrize(('sequence', 'output'), [
    ([1, 2, 3, 4], [4, 6]),
    ((1, 2, 3, 4, 5), [9, 6]),
])
def test_even_odd_sums(sequence, output):
    assert even_odd_sums(sequence) == output


@pytest.mark.parametrize(('sequence', 'output'), [
    ([10, 20, 30, 40, 50, 60], 50),
    ([1, 2, 3, 4, 5], -1),
])
def test_plus_minus(sequence, output):
    assert plus_minus(sequence) == output
