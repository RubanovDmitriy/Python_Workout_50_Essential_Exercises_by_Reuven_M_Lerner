import pytest

from exercise_32_flip_dict.exercise_32_flip_dict import flipped_dict


@pytest.mark.parametrize(('d', 'fd'), [
    ({}, {}),
    ({'a': 1}, {1: 'a'}),
    ({'a': 1, 'b': 2, 'c': 3}, {1: 'a', 2: 'b', 3: 'c'}),
])
def test_flipped_dict(d, fd):
    assert flipped_dict(d) == fd
