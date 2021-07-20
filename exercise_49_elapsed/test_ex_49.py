import time

from exercise_49_elapsed.exercise_49_elapsed import elapsed_since


def test_simple():
    for index, t in enumerate(elapsed_since('abc')):
        assert isinstance(t, tuple)
        assert isinstance(t[0], float)
        assert isinstance(t[1], str)

        if index == 0:
            assert t[0] == 0

        else:
            assert int(t[0]) == 1

        time.sleep(1)
