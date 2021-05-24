def sum_numeric(*args):
    total = 0

    for arg in args:
        try:
            total += int(arg)
        except ValueError:
            pass
    return total
