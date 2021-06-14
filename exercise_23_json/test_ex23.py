import pytest

from exercise_23_json.exercise_23_json import print_scores
from exercise_23_json.exercise_23_passwd_to_json import passwd_to_json


@pytest.fixture()
def score_file_1(tmp_path):
    j1 = tmp_path / '9a.json'
    j1.write_text('''
[{"math" : 90, "literature" : 98, "science" : 97},
 {"math" : 65, "literature" : 79, "science" : 85},
 {"math" : 78, "literature" : 83, "science" : 75},
 {"math" : 92, "literature" : 78, "science" : 85},
 {"math" : 100, "literature" : 80, "science" : 90}
]
''')
    return j1


@pytest.fixture()
def score_file_2(tmp_path):
    j2 = tmp_path / '9b.json'
    j2.write_text('''
[{"math" : 70, "literature" : 98, "science" : 97},
 {"math" : 65, "literature" : 83, "science" : 70},
 {"math" : 58, "literature" : 83, "science" : 75},
 {"math" : 72, "literature" : 78, "science" : 85},
 {"math" : 100, "literature" : 80, "science" : 90}
]
''')
    return j2


@pytest.fixture()
def empty_passwd(tmp_path):
    f = tmp_path / 'passwd'
    f.write_text('')
    return f


@pytest.fixture()
def complex_passwd(tmp_path):
    f = tmp_path / 'passwd'
    f.write_text('''root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
# this is a comment line
# and then we have some blank lines
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
''')
    return f


def test_scores(tmp_path, score_file_1, score_file_2, capsys):
    print_scores(tmp_path)
    captured_out, captured_err = capsys.readouterr()
    assert '9a.json' in captured_out
    assert '9b.json' in captured_out
    assert captured_out.count(' min ') == 6
    assert captured_out.count(' max ') == 6
    assert captured_out.count(' average ') == 6


def test_empty(empty_passwd):
    assert passwd_to_json(empty_passwd) == '[]'


def test_complex(complex_passwd):
    d = passwd_to_json(complex_passwd)
    assert len(d) == 599
    assert d[-9:] == 'ogin\\n"]]'
