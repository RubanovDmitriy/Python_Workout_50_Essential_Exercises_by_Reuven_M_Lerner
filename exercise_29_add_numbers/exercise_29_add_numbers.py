def sum_numbers(numbers):
    return sum(int(number) for number in numbers.split() if number.isdigit())
