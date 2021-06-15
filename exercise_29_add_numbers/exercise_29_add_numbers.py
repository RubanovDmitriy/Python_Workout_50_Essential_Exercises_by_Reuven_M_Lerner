def sum_numbers(numbers):
    return sum(int(number) for number in numbers.split() if number.isdigit())

print(sum_numbers('10 abc 20 de44 30 55fg 40'))