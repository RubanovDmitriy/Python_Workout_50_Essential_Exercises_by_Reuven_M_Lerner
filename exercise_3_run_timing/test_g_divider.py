import pytest

from exercise_3_run_timing.the_great_divider import divider


def test_divider():
    assert divider(1234.5678, 2, 3) == 34.567
