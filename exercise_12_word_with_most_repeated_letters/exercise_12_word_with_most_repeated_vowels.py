from collections import Counter


def most_repeating_letter_count(word):
    vowels_in_word = ''
    for letter in word.lower():
        if letter in 'aeiou':
            vowels_in_word += letter

    return Counter(vowels_in_word).most_common(1)[0][1]


def most_repeating_vowel(words):
    """
    Find the word with the greatest number of repeated vowels
    """
    return max(words, key=most_repeating_letter_count)
