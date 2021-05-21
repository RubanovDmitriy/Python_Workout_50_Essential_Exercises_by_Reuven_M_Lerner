def even_odd_sums(sequence):
    evens = []
    odds = []

    for one_number in range(len(sequence)):
        if one_number % 2:
            odds.append(sequence[one_number])
        else:
            evens.append(sequence[one_number])

    return [sum(evens), sum(odds)]
