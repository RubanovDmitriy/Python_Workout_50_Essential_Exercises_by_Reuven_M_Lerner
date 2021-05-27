from exercise_12_word_with_most_repeated_letters.exercise_12_word_with_most_repeated_letters import most_repeating_word
from exercise_12_word_with_most_repeated_letters.exercise_12_word_with_most_repeated_vowels import most_repeating_vowel


def test_most_repeating_word():
    assert most_repeating_word(['this', 'is', 'an', 'elementary', 'test', 'example']) == 'elementary'


def test_most_repeating_vowel():
    assert most_repeating_vowel(['this', 'is', 'an', 'elementary', 'test', 'example', 'aaaaa']) == 'aaaaa'
