
'''Write a function that takes a list of words (strings). It should return a tuple con-
taining three integers, representing the length of the shortest word, the length
of the longest word, and the average word length.'''


def words_to_tuple(words):
    result = 0

    sorted_list = sorted(words, key=len)

    for word in words:
        result += len(word)
        avg_word = result / len(words)

    short = len(sorted_list[0])
    average = avg_word
    long = len(sorted_list[-1])

    result_list = [short, long, average]

    return(tuple(result_list))
