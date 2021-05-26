def by_vowel_count(one_word):
    total = 0
    for one_character in one_word.lower():
        if one_character in 'aeiou':
            total += 1
    return total


def sort_strings_by_vowel_count(input_data):
    """Given a list of strings, sort them according to how many vowels they contain."""
    return sorted(input_data, key=by_vowel_count)


print(sort_strings_by_vowel_count(['eyuooo', 'abo', 'a']))
