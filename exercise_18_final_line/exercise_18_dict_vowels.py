def dict_vowels(file):
    total_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for current_line in open(file):
        fields = current_line
        for letter in fields.lower():
            if letter in total_vowels.keys():
                total_vowels[letter] += 1
                print(letter)

    return total_vowels
