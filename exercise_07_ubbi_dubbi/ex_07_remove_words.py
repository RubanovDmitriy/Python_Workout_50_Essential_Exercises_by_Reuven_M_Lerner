def remove_words(text, names):
    """Given a string (text) and a list of strings (names),
remove any occurence of a name from text and return it.
"""
    output = text

    for one_name in names:
        output = output.replace(one_name, '_' * len(one_name))

    return output


if __name__ == '__main__':
    print(remove_words('zil bil Vasia, a Petya ego pobil', ['Vasia', 'Petya']))
