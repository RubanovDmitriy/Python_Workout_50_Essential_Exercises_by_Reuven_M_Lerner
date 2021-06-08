import pytest

from exercise_17_count_diff_numbers.exercise_17_count_diff_numbers import how_many_different_numbers


@pytest.mark.parametrize(('numbers', 'result'), [
    ([], 0),
    ([10, 20, 30], 3),
    ([10, 10, 10], 1),
    ([10, 10.0, 10], 1)
])
def test_sort_absolute(numbers, result):
    assert how_many_different_numbers(numbers) == result
