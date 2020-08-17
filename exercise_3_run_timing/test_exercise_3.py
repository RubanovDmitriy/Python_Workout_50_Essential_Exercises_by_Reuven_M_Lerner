import pytest

from io import StringIO
from exercise_3_run_timing.run_timing import avg_run_time
from exercise_3_run_timing.the_great_divider import divider

'''
Надо разобаться как работать с иптом в wile loop
И почему у меня продолжает работать и валиться закоменченный тест
'''
# def test_avg_run_time(monkeypatch):
#     number_inputs = StringIO('1\n2\n3\n4\n\n')
#     monkeypatch.setattr('sys.stdin', number_inputs)
#     assert avg_run_time() == 'Average of 2.5, over 4 runs'


def test_divider():
    assert divider(1234.5678, 2, 3) == 34.567
