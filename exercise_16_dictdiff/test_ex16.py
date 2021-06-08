import pytest

from exercise_16_dictdiff.exercise_16_dictdiff import dictdiff
from exercise_16_dictdiff.exercise_16_even_odd_dicts import even_odd_dicts
from exercise_16_dictdiff.exercise_16_multiupdate import multiupdate


@pytest.fixture()
def simple_dict1():
    return {'a': 1, 'b': 2, 'c': 3}


@pytest.fixture()
def simple_dict2():
    return {'a': 1, 'b': 2, 'c': 4}


@pytest.fixture()
def simple_dict3():
    return {'a': 3, 'k': 5, 'e': 8}


def test_empty():
    assert dictdiff({}, {}) == {}


def test_same(simple_dict1):
    assert dictdiff(simple_dict1, simple_dict1) == {}


def test_simple_diff(simple_dict1, simple_dict2):
    assert dictdiff(simple_dict1, simple_dict2) == {'c': [3, 4]}


def test_multiupdate(simple_dict1, simple_dict2, simple_dict3):
    assert multiupdate(simple_dict1, simple_dict2, simple_dict3) == {'a': 3, 'b': 2, 'c': 4, 'k': 5, 'e': 8}


@pytest.mark.parametrize(('args', 'result'), [
    (['a', 1, 'b', 2], {'a': 1, 'b': 2}),
])
def test_sort_absolute(args, result):
    assert even_odd_dicts(args) == result
