import string


def ubbi_dubbi_capital(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    list_word = []
    for letter in word:
        if letter in vowels:
            list_word.append(f'ub{letter}')
        else:
            list_word.append(letter)

    final_result = ''.join(list_word)

    if word[0] in string.ascii_uppercase:
        list_word[0] = list_word[0].capitalize()

    return final_result


if __name__ == '__main__':
    print(ubbi_dubbi_capital('Version'))
