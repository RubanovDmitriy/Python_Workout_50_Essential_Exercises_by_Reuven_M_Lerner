def ubbi_dubbi(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    list_word = []
    for letter in word:
        if letter in vowels:
            list_word.append(f'ub{letter}')
        else:
            list_word.append(letter)

    return ''.join(list_word)


if __name__ == '__main__':
    print(ubbi_dubbi('python'))
