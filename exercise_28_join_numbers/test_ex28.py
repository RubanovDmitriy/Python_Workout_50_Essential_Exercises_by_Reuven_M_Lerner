import pytest

from exercise_28_join_numbers.exercise_28_join_numbers import join_numbers
from exercise_28_join_numbers.exercise_28_join_ten_numbers import join_ten_numbers


@pytest.mark.parametrize(('seq', 'string'), [
    (range(15), '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14'),
    (range(10, 15), '10,11,12,13,14'),
    (range(0), '')
])
def test_join_numbers(seq, string):
    assert join_numbers(seq) == string


@pytest.mark.parametrize(('seq', 'string'), [
    (range(15), '0,1,2,3,4,5,6,7,8,9,10'),
    (range(10, 15), '10'),
    (range(0), '')
])
def test_join_ten_numbers(seq, string):
    assert join_ten_numbers(seq) == string
