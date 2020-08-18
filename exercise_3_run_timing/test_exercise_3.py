from exercise_3_run_timing.ex03p2_decimal_add import decimal_add
from exercise_3_run_timing.the_great_divider import divider


def test_divider():
    assert divider(1234.5678, 2, 3) == 34.567


def test_decimal_add():
    assert decimal_add('1.3', '2.4') == 3.7
