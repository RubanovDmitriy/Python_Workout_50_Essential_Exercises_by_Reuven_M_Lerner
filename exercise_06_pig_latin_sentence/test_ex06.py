import pytest
from exercise_06_pig_latin_sentence.ex06_pig_latin_sentence import pl_sentence


@pytest.mark.parametrize('input_word, output_word', [
    ('this is a test translation', 'histay isway away esttay ranslationtay'),
    ('elephant', 'elephantway'),
    ('this is a test', 'histay isway away esttay'),
])
def test_pig_latin_sentence(input_word, output_word):
    assert pl_sentence(input_word) == output_word
