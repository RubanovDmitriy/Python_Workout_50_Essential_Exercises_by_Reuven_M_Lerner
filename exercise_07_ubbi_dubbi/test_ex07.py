import pytest
from exercise_07_ubbi_dubbi.ex_07_ubbi_dubbi import ubbi_dubbi


@pytest.mark.parametrize('input_word, output_word', [
    ('sosiska', 'subosubiskuba'),
    ('loop', 'luboubop'),
    ('password', 'pubasswubord'),
    ('python', 'pythubon'),
    ('motherboard', 'mubothuberbuboubard')
])
def test_ubbi_dubbi(input_word, output_word):
    assert ubbi_dubbi(input_word) == output_word
