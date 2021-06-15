import pytest

from exercise_29_add_numbers.exercise_29_add_numbers import sum_numbers


@pytest.mark.parametrize('numbers, total', [
    ('10 20 30', 60),
    ('10 abc 30', 40),
    ('10 abc 20 de44 30 55fg 40', 100)
])
def test_sum_numbers(numbers, total):
    assert sum_numbers(numbers) == total
