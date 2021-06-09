
import pytest

from exercise_20_wc.exercise_20_wc import wordcount


@pytest.fixture()
def empty_file(tmp_path):
    f = tmp_path / 'textfile'
    f.write_text('')
    return f


@pytest.fixture()
def simple_file(tmp_path):
    f = tmp_path / 'wcfile.txt'
    f.write_text('''This is a test file.
It contains 28 words and 20 different words.
It also contains 165 characters.
It also contains 11 lines.
It is also self-referential.
Wow!''')
    return f


def test_empty(empty_file, capsys):
    wordcount(empty_file)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == """lines: 0
characters: 0
word_count: 0
unique words: 0
"""


def test_simple(simple_file, capsys):
    wordcount(simple_file)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == """lines: 6
characters: 159
word_count: 28
unique words: 20
"""
