import pytest

from exercise_11_alphabetizing_names.exercise_11_alphabetizing_names import alphabetize_names, PEOPLE
from exercise_11_alphabetizing_names.exercise_11_sort_abs_numbers import sort_absolute
from exercise_11_alphabetizing_names.exercise_11_sort_by_sum import sort_by_sum
from exercise_11_alphabetizing_names.exercise_11_sort_strings_by_vowel_count import sort_strings_by_vowel_count


def test_empty():
    assert alphabetize_names([]) == []


def test_with_people():
    assert PEOPLE[0]['last'] == 'Lerner'
    assert PEOPLE[1]['last'] == 'Trump'
    assert PEOPLE[2]['last'] == 'Putin'

    output = alphabetize_names(PEOPLE)
    assert output[0]['last'] == 'Lerner'
    assert output[1]['last'] == 'Putin'
    assert output[2]['last'] == 'Trump'


@pytest.mark.parametrize(('numbers', 'sorted_numbers'), [
    ([1, 55, -999, 5, 6, 78], [1, 5, 6, 55, 78, -999]),
    ([2, 43, -7, 52, 16, 87], [2, -7, 16, 43, 52, 87]),
    ([], []),
])
def test_sort_absolute(numbers, sorted_numbers):
    assert sort_absolute(numbers) == sorted_numbers


@pytest.mark.parametrize(('input', 'output'), [
    (['eyuoo', 'abo', 'a'], ['a', 'abo', 'eyuoo']),
])
def test_sort_strings_by_vowel_count(input, output):
    assert sort_strings_by_vowel_count(input) == output


def test_sort_by_sum():
    assert sort_by_sum([[1, 3, 99], [4, 8, 1, 44], [999, 5, 77]]) == [[4, 8, 1, 44], [1, 3, 99], [999, 5, 77]]
