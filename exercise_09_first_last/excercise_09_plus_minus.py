def plus_minus(numbers):
    if not numbers:
        return 0

    total = numbers.pop(0)

    while numbers:
        total += numbers.pop(0)

        if numbers:
            total -= numbers.pop(0)

    return total
