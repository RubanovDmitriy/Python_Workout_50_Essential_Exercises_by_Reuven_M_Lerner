def sum_ints(file):
    total = 0
    for current_line in open(file):
        for letter in current_line:
            if letter.isdigit():
                total += int(letter)

    return total
