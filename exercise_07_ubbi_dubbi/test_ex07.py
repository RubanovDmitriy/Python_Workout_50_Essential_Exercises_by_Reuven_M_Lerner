import pytest

from exercise_07_ubbi_dubbi.ex_07_ubbi_dubbi import ubbi_dubbi
from exercise_07_ubbi_dubbi.ex_07_ubbi_dubbi_capital import ubbi_dubbi_capital


@pytest.mark.parametrize(('input_word', 'output_word'), [
    ('sosiska', 'subosubiskuba'),
    ('loop', 'luboubop'),
    ('password', 'pubasswubord'),
    ('python', 'pythubon'),
    ('motherboard', 'mubothuberbuboubard')
])
def test_ubbi_dubbi(input_word, output_word):
    assert ubbi_dubbi(input_word) == output_word


@pytest.mark.parametrize(('input_word', 'output_word'), [
    ('Characters', 'Chubarubactubers'),
    ('respectively', 'rubespubectubivubely'),
    ('Append', 'Appubend'),
    ('modified', 'mubodubifubiubed'),
    ('Version', 'Vubersubiubon')
])
def test_ubbi_dubbi_capital(input_word, output_word):
    assert ubbi_dubbi_capital(input_word) == output_word
