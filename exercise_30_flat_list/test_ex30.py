import pytest

from exercise_30_flat_list.exercise_30_flat_list import flatten


@pytest.mark.parametrize(('nested', 'output'), [
    ([[10, 20, 30]], [10, 20, 30]),
    ([[10, 20], [30, 40]], [10, 20, 30, 40]),
])
def test_flatten(nested, output):
    assert flatten(nested) == output
