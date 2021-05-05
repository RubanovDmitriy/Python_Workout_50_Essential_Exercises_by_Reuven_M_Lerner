'''Write a function that takes a list of numbers. It should return the average (i.e.,
arithmetic mean) of those numbers.'''


def mysum(numbers, start=0):
    result = start
    lenght = len(numbers)
    for ele in range(0, len(numbers)):
        result = result + numbers[ele]
    return result / lenght
