'''Write a function that takes a float and two integers ( before and after ). The
function should return a float consisting of before digits before the decimal
point and after digits after. Thus, if we call the function with 1234.5678 , 2 and
3 , the return value should be 34.567'''


def divider(number: float,
            before: int,
            after: int):

    to_string = str(number)
    dot = to_string.index('.')

    return float(to_string[dot - before: dot + after + 1])


divider(1234.1234, 2, 3)
