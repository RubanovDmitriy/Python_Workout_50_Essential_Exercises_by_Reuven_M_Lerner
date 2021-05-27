from collections import Counter


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    """
    Function that takes a sequence of strings as input.
    The function should return the string that contains the greatest number of repeated letters
    """
    return max(words, key=most_repeating_letter_count)
