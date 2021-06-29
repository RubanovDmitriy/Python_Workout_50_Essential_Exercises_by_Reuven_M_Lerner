from exercise_42_flex_dict.exercise_42_flex_dict import FlexibleDict
from exercise_42_flex_dict.exercise_42_str_flex_dict import StringKeyDict


def test_flexible_dict():
    fd = FlexibleDict()

    fd['a'] = 100
    assert fd['a'] == 100

    fd[5] = 500
    assert fd[5] == 500

    fd[1] = 100
    assert fd[1] == 100
    assert fd['1'] == 100

    fd['1'] = 100
    assert fd[1] == 100
    assert fd['1'] == 100


def test_string_key_dict():
    skd = StringKeyDict()

    skd[1] = 10
    assert skd['1'] == 10
