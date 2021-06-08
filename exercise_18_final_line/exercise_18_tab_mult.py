def tab_mult(file):
    total = 0

    for current_line in open(file):
        fields = current_line.split()

        if len(fields) != 2:
            continue

        first, second = fields

        if not first.isdigit():
            continue

        if not second.isdigit():
            continue

        total += int(first) * int(second)

    return total
