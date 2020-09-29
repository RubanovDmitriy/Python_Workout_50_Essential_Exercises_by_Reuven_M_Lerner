vowels = ('a', 'e', 'i', 'o', 'u')
list_sentence = []


def pl_sentence(sentence):
    for word in sentence.split():
        if word[0] in vowels:
            list_sentence.append(f'{word}way')
        else:
            list_sentence.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(list_sentence)


if __name__ == '__main__':
    print(pl_sentence('this is a test translation'))
