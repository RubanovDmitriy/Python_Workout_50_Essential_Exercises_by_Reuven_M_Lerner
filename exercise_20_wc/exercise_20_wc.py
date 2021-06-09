def wordcount(filename):
    result_dict = {
        'lines': 0,
        'characters': 0,
        'word_count': 0,
    }
    unique_words = set()

    for line in open(filename):
        result_dict['lines'] += 1
        result_dict['characters'] += len(line)
        result_dict['word_count'] += len(line.split())
        unique_words.update(line.split())
    result_dict['unique words'] = len(unique_words)
    for key, value in result_dict.items():
        print(f'{key}: {value}')
