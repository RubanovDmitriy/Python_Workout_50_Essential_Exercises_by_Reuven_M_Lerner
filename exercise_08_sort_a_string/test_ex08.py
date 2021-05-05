import pytest

from exercise_08_sort_a_string.ex_08_sort_a_string import strsort


@pytest.mark.parametrize(('input_word', 'output_word'), [
    ('abcdef', 'abcdef'),
    ('abcDEF', 'DEFabc'),
    ('ab c', ' abc'),
    ('abcdefabcdef', 'aabbccddeeff')
])
def test_strsort(input_word, output_word):
    assert strsort(input_word) == output_word
