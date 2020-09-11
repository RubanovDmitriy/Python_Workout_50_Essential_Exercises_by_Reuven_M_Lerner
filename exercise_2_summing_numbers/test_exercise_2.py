
import pytest

from exercise_2_summing_numbers.summing_numbers_4 import words_to_tuple


def test_words_to_tupple():
    assert words_to_tuple(['privet', 'kot', 'tvoi_rot', 'rakamakafo']) == (3, 10, 6.75)