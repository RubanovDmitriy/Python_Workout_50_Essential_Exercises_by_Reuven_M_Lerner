import pytest

from exercise_25_xml.exercise_25_factorial import factorial
from exercise_25_xml.exercise_25_xml import myxml


def test_tagonly():
    assert myxml('tagname') == '<tagname></tagname>'


def test_tag_simple_text():
    assert myxml('tagname', 'text') == '<tagname>text</tagname>'


def test_nested():
    assert myxml('a',
                 myxml('b',
                       myxml('c', 'text'))) == '<a><b><c>text</c></b></a>'


def test_attributes():
    assert myxml('tagname',
                 a=1, b=2, c=3) == '<tagname a="1" b="2" c="3"></tagname>'


def test_attributes_and_text():
    assert myxml('tagname', 'text',
                 a=1, b=2, c=3) == '<tagname a="1" b="2" c="3">text</tagname>'


@pytest.mark.parametrize(('args', 'output'), [
    ((1, 2, 3), 6),
    ((0, 66, 99), 0),
    ((3, 2, 4), 24)
])
def test_factorial(args, output):
    assert factorial(args) == output
