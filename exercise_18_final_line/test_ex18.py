import pytest

from exercise_18_final_line.exercise_18_dict_vowels import dict_vowels
from exercise_18_final_line.exercise_18_final_line import get_final_line
from exercise_18_final_line.exercise_18_sum_ints import sum_ints
from exercise_18_final_line.exercise_18_tab_mult import tab_mult


@pytest.fixture()
def fakefile(tmp_path):
    f = tmp_path / 'filename.txt'
    f.write_text('vEmrN2vCPbS4S3yU\n2dSBSPgaDTJlucqY\nUXzBCCqJoKwOgN86\nKHD4oQHW2yVmoUDE\nZOdqJkTMU5yGJns7'
                 'MxlmXRiIZKPmMHoa\nMFnLQVyhXeFWMfM6\nsxJ9MFdF7XssdOTQ\npNhGauOtsG1QsysT\n91KU9IcyxBRmfslP')
    return f


@pytest.fixture()
def empty_file(tmp_path):
    f = tmp_path / 'filename.txt'
    f.write_text('')
    return f


@pytest.fixture()
def simple_file(tmp_path):
    f = tmp_path / 'filename.txt'
    f.write_text('abcd\nefgh\nijkl\n')
    return f


@pytest.fixture()
def tab_fake(tmp_path):
    f = tmp_path / 'filename.txt'
    f.write_text('1\t2\n3\t4\n5\t6\na\t7\n8\t9\n10\n')
    return f


def test_empty(empty_file):
    assert get_final_line(empty_file) == ''


def test_simple(simple_file):
    assert get_final_line(simple_file) == 'ijkl\n'


def test_get_final_line(fakefile):
    assert get_final_line(fakefile) == '91KU9IcyxBRmfslP'


def test_sum_ints(fakefile):
    assert sum_ints(fakefile) == 85


def test_tab_mult(tab_fake):
    assert tab_mult(tab_fake) == 116


def test_dict_vowels(fakefile):
    assert dict_vowels(fakefile) == {'a': 3, 'e': 3, 'i': 3, 'o': 8, 'u': 7}
