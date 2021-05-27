import pytest

from exercise_13_printing_tuple_records.exercise_13_printing_tuple_records import format_sort_records


@pytest.mark.parametrize(('input', 'output'), [
    ([('Donald', 'Trump', 7.85),
      ('Vladimir', 'Putin', 3.626),
      ('Jinping', 'Xi', 10.603)],
     ['Putin      Vladimir    3.63',
      'Trump      Donald      7.85',
      'Xi         Jinping    10.60']),
])
def test_format_sort_records(input, output):
    assert format_sort_records(input) == output
