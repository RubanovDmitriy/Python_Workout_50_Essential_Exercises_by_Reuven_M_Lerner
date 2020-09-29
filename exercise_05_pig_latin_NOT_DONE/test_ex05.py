import pytest
from exercise_05_pig_latin_NOT_DONE.ex05_pig_latin import pig_latin


@pytest.mark.parametrize('input_word, output_word', [
    ('computer', 'omputercay'),
    ('table', 'abletay'),
    ('papaya', 'apayapay'),
    ('elephant', 'elephantway'),
    ('octopus', 'octopusway'),
    ('insightful', 'insightfulway')
])
def test_pig_latin(input_word, output_word):
    assert pig_latin(input_word) == output_word
